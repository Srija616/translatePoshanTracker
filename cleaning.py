# run this file only after aligning data - by modifying the script in align.py
# To run this file, your data must be aligned, i.e. in each row the Indic sentence should be a translation of the English sentence

import pandas as pd
from ftlangdetect import detect
import utils
import os
import config
from multiprocessing import Pool
import fasttext
fasttext.FastText.eprint = lambda x: None # added to suppress an unnecessary warning

# for marking purposes: use the directory abc which has aligned but unclean data
# NOTE: splitting using the indic-NLP library is performed as part of web scraping itself.

directory = config.raw_data_new_directory
save_directory = config.raw_data_new_directory
directory_unsupported = config.unsupported_directory

    
def process_supported_files(args):
    file, save_directory = args
    language_code = file[3:-4]  # en_hi.csv format of files
    print (f"Processing for {language_code}")
    df = pd.read_csv(os.path.join(directory, file), encoding = 'utf-8')
    df.drop_duplicates(inplace=True) 
    count = df[df.columns[1]].count()
    new_df = df[(df[language_code].apply(lambda x: detect(x)['lang']) != "en") & (~df[language_code].str.isnumeric()) & (df['en'].str.len() >= 2)]
    new_count = new_df[language_code].count()
    print (F"language_code: {language_code}, count_new: {len(new_df)}, count_old: {count}")
    
    # detect language
    length = min(100, new_count)
    text_string = ' '.join([str(elem) for elem in new_df[language_code][:length]]) 
    detected_language = utils.detect_language(text_string)  # fix this line
    
    new_df = pd.DataFrame(new_df, columns=["en", language_code])
    new_df.to_csv(os.path.join(save_directory , file), index= False)
    
    return [language_code, detected_language]
    

def process_unsupported_files(file):
    language_code = file[:-4]
    print (f"Processing for: {language_code}")
    df = pd.read_csv(os.path.join(directory_unsupported, file), encoding = 'utf-8')
    new_df = df["data"].to_list()  # new_df data is monolingual 
    text_string = ' '.join([str(elem) for elem in new_df[:100]])
    detected_language = utils.detect_language(text_string)  # fix this line
    return [language_code, detected_language]

    
if __name__ == '__main__':

    with Pool(processes=config.default_num_processes) as pool:
        results = pool.map(process_supported_files, [file for file in os.listdir(directory)])
        
    with Pool (processes=config.default_num_processes) as pool:
        results_unsupported = pool.map(process_unsupported_files, [file for file in os.listdir(directory_unsupported)])

    results.extend(results_unsupported)
    lang_deteced = pd.DataFrame(results, columns = ["original_language", "detected_langauge"])
    lang_deteced.to_csv("language_detected.csv")