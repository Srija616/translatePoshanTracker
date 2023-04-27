# Translation Inference - PoshanTracker Website

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#task1">Task 1</a></li>
    <li><a href="#task2">Task 2</a></li>
    <li><a href="#task3">Task 3</a></li>
    <li><a href="#task4">Task 4</a></li>
    <li><a href="#task5">Task 5</a></li>
    <li><a href="#observations">Observations</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
The project scrapes the data from [PoshanTracker](https://www.poshantracker.in/) website to create a parallel dataset of English-Indic language format. The Indic language data is then translated to English using two different models - [indicTrans](https://github.com/AI4Bharat/indicTrans) and [helsinki-nlp/opus-mt-mul-en](https://huggingface.co/Helsinki-NLP/opus-mt-mul-en). Finally, the BLEU scores and CHRF scores are calculated.

Here is a list of all webpages scraped:
|No. | Webpage  |
|----| ------------- | 
|1. | https://www.poshantracker.in/ | 
|2. | https://www.poshantracker.in/resources | 
|3. |https://www.poshantracker.in/aboutus |
|4. |https://www.poshantracker.in/contactus |
|5. |https://www.poshantracker.in/pocalculator |
|6. |https://www.poshantracker.in/vaccinationschedule |
|7. |https://www.poshantracker.in/statistics| 
|8. |https://www.poshantracker.in/KpiLogin |
|9. |https://www.poshantracker.in/support/ |
|10. |https://www.poshantracker.in/faq/ |
|11. |https://www.poshantracker.in/ptcalculator/ |

<!-- GETTING STARTED -->
## Getting Started
Assuming you have pip, python, pandas and numpy installed,
1. Clone the repository
  ```sh
   git clone https://github.com/Srija616/translationTask.git
   ```
 2. Install the requirements:
 ```sh
   pip install -r requirements.txt
   ```
 3. For task 1, 2 and 3, indic-nlp library and indicTrans translation model is required, so run the script.sh file
 ```sh
   bash script.sh
   ```
 Note: After cloning indicTrans, please add __init__.py file in the indicTrans directory. Also change the import statement in indicTrans\inference\engine.py:   ```from inference.custom_interactive import Translator``` to ```from indicTrans.inference.custom_interactive import Translator```

<!-- Task 1 -->
## Task 1 - Downloading the data

After installing the requirements, run the **web_scraper.py** file. The web_scraper.py module extracts data from [PoshanTracker](https://www.poshantracker.in/) and its internally linked webpages.

The extracted data is divided into three sets:
1. **raw_data** - it consists of **bilingual** csv files in the format en-indiclang. raw_data is cleaned manually (or with a small script - **align.py**) to align the data. Using **cleaning.py**, the data is finally processed in Task 2 to remove duplicates and data from other languages (especially separating English data from Indic data) </br>
Languages: ['bn', 'gu', 'hi', 'kn', 'ml', 'mr', 'or', 'pa', 'ta', 'te'] i.e. [Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Panjabi, Tamil, Telugu]
2. **unsupported_clean**: For languages that are not supported by fasttext-langdetect, **monolingual data** is cleaned to remove duplicates, numeric text and text with less than 2 characters and added here.</br>
Languages: ['as', 'ne', 'doi', 'kok', 'sd', 'brx', 'mai', 'mni', 'sat', 'ur', 'ks'] i.e. [Assamese, Nepali, Dogri, Konkani, Sindhi, Bodo, Maithili, Manipuri, Santhali, Urdu, Kashmiri]
3. **supported_clean**: For languages supported by fasttext-langdetect and also in the common_supported languages (i.e. translation is supported by both indicTrans and Helsinki), **monolingual** data is cleaned to remove other languages, duplicates, numeric text and text with less than 2 characters and added here. </br>
Languages: ['bn', 'gu', 'hi', 'kn', 'ml', 'mr', 'or', 'pa', 'ta', 'te', 'en'] i.e. [Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Panjabi, Tamil, Telugu, English]

To generalize the process of scraping the data, change the function **get_language_driver** in **web_scraper.py** according to your website. Also, in the **config.py** module, change the list variable **languages** and **langugae_codes** according to your website. You may include only one language as well. 
In the repository I have added the result for scraping www.google.com in the **scrape_external.csv** file. If you do not wish to make call to **get_language_driver**, comment out the following code block in **get_all_data** function.

```
try:
    driver = get_language_driver(lang, driver, url) 
except:
    print (f"Unable to get a language driver for {language_isocode}, possibly you have sent too many get requests in a short time and getting HTTP 429 error")
    return []
```

<!-- Task 2 -->
## Task 2 - Preprocessing data
Input directory: **raw_data**  (It contains the output of Task 1 which is in turn processed semi-automated using align.py) </br>
Output directory: **raw_data_new** </br>
After aligning the text in **raw_data** with the help of **align.py**, clean the text using **cleaning.py**

For testing purposes, use **raw_data_new** as the input directory as well.
**cleaning.py** performs the following tasks:
1. Preprocessing - Remove duplicates, remove data from other languages, remove data that is numeric or of length less than 2 characters.
2. Language detection - Done for all languages irrespective of support with the **fasttext-langdetect** library.  </br>

**NOTE:** As evident, low resource languages that share script or word similarities with a high resource language, example, Maithili and Sindhi with Hindi or Konkani with Marathi, Manipuri with Bengali are detected as their respective high-resource language. It is important to note that the library officially supports Sindhi and Maithili, yet fail to detect them correctly, even though complete data was provided for detection. Also, unsupported languages like Dogri, Bodo and Santhali are detected as English.

|Language - original | Language - Detected |
|----| ------------- | 
|Bengali| Bengali |
|Gujarati | Gujarati |
|Hindi | Hindi |
|Kannada | Kannada |
|Malayalam | Malayalam|
|Marathi | Marathi|
|Odia | Odia |
|Panjabi |Panjabi |
|Tamil | Tamil |
|Telugu | Telugu |
|Assamese | Assamese |
|Bodo | English |
|Dogri | English |
|Konkani | Marathi |
|Maithili | Hindi |
|Manipuri | Bengali |
|Nepali | Nepali |
|Santhali | English |
|Sindhi | Hindi |
|Urdu | Urdu |
|Kashmiri | Urdu |

<!-- Task 3 -->
## Task 3 - Translations using IndicTrans
Run the code **indicTrans.py** and the output is stored in directory **translated_indicTrans**

<!-- Task 4 -->
## Task 4 - Translations using helsinki-nlp/opus-mt-mul-en 

Run the code **helsinki.py** and the output is stored in directory **translated_helsinki**

<!-- Task 5 -->
## Task 5 - Bleu and CHRF scores
Run  **calculate_metrics.py** to get the CHRF and BLEU scores.

|No. |language_code|bleu_indicTrans   |chrf_indicTrans   |bleu_helsinki     |chrf_helsinki     |
|------|-------------|------------------|------------------|------------------|------------------|
|1     |bn           |40.361451397114195|67.29100086720587 |15.008718294521943|38.459893968335855|
|2     |gu           |40.09242647814781 |62.38047934152201 |17.519435117029424|41.67385242030943 |
|3     |hi           |35.46963979966534 |61.12925209053163 |11.225427865557949|38.59222728367872 |
|4     |kn           |32.147355804677694|56.59004522220443 |15.618151502462212|38.06799170855191 |
|5     |ml           |37.8225649633747  |61.7368338997521  |15.2814778557767  |39.55520687508669 |
|6     |mr           |36.618912232159545|61.060112673233135|15.732443365648534|40.030517925746025|
|7     |or           |40.61712977226381 |64.53967600298299 |11.310679447675124|36.57590226441299 |
|8     |pa           |33.19827639988097 |56.28109096317498 |16.424478002794018|40.2022064113979  |
|9     |ta           |32.618353590741094|55.570154385196666|14.990324396869909|38.452540317035634|
|10     |te           |39.97781730506786 |62.885759163173674|20.18320840530373 |43.50483959356902 |


<!-- Observations -->
## Inferences and observations

My observations on the translations:
1. The translations by indicTrans are far better for most of the Indic languages in comparison to helsinki-nlp/opus-mt-mul-en
2. helsinki-nlp/opus-mt-mul-en produces garbage text for certain languages like Bengali and Odia. Eg: "State Helpdesk" in Bengali is translated to "The Kingdom Hall of Jehovah’s Witnesses"
3. Some words don't seem to be a part of the vocabulary, however indicTrans does a better job at Transliteration when it cannot translate, compared to Helsinki model. However, I also noticed that words like "Poshan" is translated into different words like "Posian" or "Posan" or "animal" [Refer Bengali translations]. 
4. indicTrans adds certain character like %s or (s) before or after translations. While the translation itself is correct, but this could affect the Bleu and CHRF scores.
5. There is a difference in the amount of data for each language which can affect the scores. This was due to differences during extraction of data from website.
6. While absolute scores may not paint a correct picture, comparison of the scores for Helsinki and indicTrans is in sync with my own obeservations of data. IndicTrans is significantly better than Helsinki-NLP/opus-mt-mul-en.

Observations for the project
1. While cleaning data for each language was not difficult however ensuring that all data gets extracted from the website and aligning it with the English text was challenging and required looking at each csv individually. After manually cleaning a number of languages, I could see patterns and guesstimate the indices and text around which the alignment could have gone wrong. I have not delved deeper into why this was particularly happening in some of the languages (since the errors were not consistent across the languages), looking at how the website adds these data could help.




