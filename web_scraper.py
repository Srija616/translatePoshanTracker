from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import multiprocessing
import os
import config
import utils
from bs4 import BeautifulSoup
import pandas as pd
import time
import fasttext

fasttext.FastText.eprint = lambda x: None # added to suppress an unnecessary warning

def save_data(directory, file, text):
    file_path = os.path.join(directory, file)
    text.to_csv(file_path, index=False)
    return
   
    
def extract_text_data(driver, url, visited_urls, url_main):
    '''
    Function to scrape data from input url and other internal urls present on the webpage.
    The function does not return any value, instead the scraped text is stored in all_text string.
    
    Arguments:
    driver: Initialized Chrome Webdriver
    url (string): The url of webpage to be scraped
    visited_urls (set): Set of urls already scraped for a given language
    all_text (string): Contains all the text scraped for webpages. 
    
    Output:
    text_data: Returns a string of all scraped data, where each scraped element is delimited by '\n' character
    
    '''
    if url in visited_urls:
        return ""
    visited_urls.add(url)
    driver.get(url)
    driver.implicitly_wait(10)
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    text_data = soup.body.get_text("\n")

    for link in soup.find_all('a'):
        driver.implicitly_wait(5)
        href = link.get('href')
        driver.implicitly_wait(5)
        try:
            if href.startswith("/"): # only follow internal links to get all data
                data = extract_text_data(driver, url_main + href, visited_urls, url_main)
                if (data != ""):
                        text_data = text_data + "\n "+ (data)
        except Exception as e:
            continue
    return text_data


def get_language_driver(language, driver, url):
    '''
    The function changes the language of the website by opening the dropdown menu on the website and selecting the required language
    
    Arguments:
    language: The language for website to be scraped.
    driver: To interact with the browser
    url: The url of website to be scraped
    
    Output
    driver: Returns the driver to the website
    ''' 
    
    driver.get(url)
    driver.implicitly_wait(5)
    try:
        dropdown = driver.find_element('xpath',"//div[@class='language-dropdown dropdown-menu']") # find the dropdown menu
    except:
        time.sleep(20)
        driver.refresh()
        driver.get(url)
        driver.implicitly_wait(5)
        dropdown = driver.find_element('xpath',"//div[@class='language-dropdown dropdown-menu']") # find the dropdown menu
    
    # if the line 99 still throws an error, it will be handled by the try-except block of caller.
    
    driver.execute_script("arguments[0].style.display = 'block';", dropdown) # bring the dropdown menu on page
    driver.implicitly_wait(10)
    dropdown.click()
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='{}']".format(language)))  # get the option to be clicked
    )
    option.click()
    return driver


def process_language(args):
    '''
    Processes data for each language in the following steps:
    1. Extract Data
    2. If the language is supported by Indic-NLP Library, split the text into sentences using the split_sentence function
    3. Detect the language of text using fasttext-detect library.
    4. Now we tackle data in three different ways:
        a. If the language is supported by fasttext-detect library, remove data in the text from other languages, remove numeric strings, 
            and remove duplicates. Save this monolingual data.
        b. If the language is not supported by fasttext-detec library, removing data from other languages can be quite inaccurate, 
            therefore only numeric strings and duplicates are removed.
        c. If the language is common to both our models (indicTrans and opus-mt-mul-en),
            we have kept a copy (split_text), without any transformations which is directly used for creating the parallel data
    
    Arguments:
    language (string): The language for website to be scraped.
    driver (ChromeDriver): To interact with the browser
    url (string): The url of website to be scraped
    url_main (string): The homepage of the website
    
    Output:
    driver (ChromeDriver): Returns the driver to the website
    '''   
    lang, language_isocode, url, url_main = args
    options = Options()
    options.headless = True  # to run the code in background, without opening a browser window
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # to remove a USB related warning message
    driver = webdriver.Chrome(options=options)
    print (f"Processing text for  {language_isocode}")
    
    try:
        driver = get_language_driver(lang, driver, url) 
    except:
        print (f"Unable to get a language driver for {language_isocode}, possibly you have sent too many get requests in a short time and getting HTTP 429 error")
        return []
    
    visited_urls = set()
    all_text = extract_text_data(driver, url, visited_urls, url_main) # all_text is a string
    driver.quit()
    
    # common_supported_languages is intersection of languages supported by both indicTrans and Helsinki - which are also supported by indicNLP library
    if language_isocode in config.common_supported_languages: 
        split_text = utils.split_sentences(all_text, language_isocode)
    else:
        split_text = all_text.split("\n")
    
    print (f"number of sentences found for {language_isocode}: {len(split_text)}")

    if language_isocode in config.common_supported_languages: # supported by fastText because we use the detect function
        text_list = utils.remove_other_languages(split_text, language_isocode)
        text_list = utils.clean_data(text_list)
        text_list = pd.DataFrame({'data': text_list, 'language': language_isocode})
        text_list.drop_duplicates(keep = 'first', inplace= True, ignore_index= True)
        save_data("clean_supported", language_isocode + ".csv", text_list)
        
    else:
        text_list = utils.clean_data(split_text) # cannot remove other languages because the text language itself is not supported
        text_list = pd.DataFrame({'data': text_list, 'language': language_isocode})
        text_list.drop_duplicates(keep = 'first', inplace= True, ignore_index= True)
        save_data("clean_unsupported", language_isocode + ".csv", text_list)

    return split_text


def get_all_data(url, directory):
    '''
    Given the url, this function extracts all the data and performs the following preprocessing tasks:
    1. Detect language of the extracted data, remove text from other languages from the data.
    2. Store data such that each sentence is one row of the data
    3. Store the data in txt files.
    
    Arguments:
    url : The url of website to be scraped
    directory : The directory where you want to save the output
    
    Output:
    No output. The extracted data is stored in 'directory' folder
    '''

    if len(config.languages) != 0:
        lang_dict = dict(zip(config.languages, config.language_codes)) # key: language on website, language_codes = iso_code for the language
        languages = [lang_dict[lang] for lang in config.languages] # list of all language codes to be used
        num_processes = min(os.cpu_count(), config.default_num_processes)
        print (f"Number of processes: {num_processes}")
        
        with multiprocessing.Pool(processes=num_processes) as pool:
            data = pool.map(process_language, [(lang, lang_dict[lang], url, url_main) for lang in config.languages]) # get all data from websites.
        
        eng = 'en'
        if eng in languages:
        # code block to save the extracted data in csv files
            index_en = languages.index(eng)
            df_en=pd.DataFrame(data=data[index_en],columns=[languages[index_en]])
            
            for i in  range(len(languages)):
                if languages[i] != eng:
                    df_temp = pd.DataFrame(data=data[i],columns=[languages[i]])
                    df = pd.concat([df_en, df_temp], axis=1)
                    file = "en_" + languages[i] + ".csv"
                    save_data(directory, file, df)
    return 


if __name__ == "__main__":
    url_main = config.url_main
    directory = config.raw_data_directory
    get_all_data(url_main, directory)
    
