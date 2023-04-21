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
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#Code">Code</a></li>
      </ul>
    </li>
    <li><a href="#task1">Task 1</a></li>
    <li><a href="#task2">Task 2</a></li>
    <li><a href="#task3">Task 3</a></li>
    <li><a href="#task4">Task 4</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
The project scrapes the data from [PoshanTracker] (https://www.poshantracker.in/) website to create a parallel dataset of English-Indic language format. The Indic language data is then translated to English using two different models - [indicTrans] (https://github.com/AI4Bharat/indicTrans) and [helsinki-nlp/opus-mt-mul-en ] (helsinki-nlp/opus-mt-mul-en ). Finally, the BLEU scores and CHRF scores are calculated.

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
Assuming you have pip and python installed,
1. Clone the repository
  ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
 2. Install the requirements:
 ```sh
   pip install -r requirements.txt
   ```
 3. For task 1, 2 and 3, indic-nlp library and indicTrans translation model is required, so run the script.sh file
 ```sh
   bash script.sh
   ```
<!-- Task 1 -->
## Downloading the data

After installing the requirements, run the web_scraper.py file. The web_scraper.py module extracts data from [PoshanTracker] (https://www.poshantracker.in/) and its internally linked webpages.
The extracted data is divided into three sets:
1. Data stored in raw_data - it consists of csv files in the format en-indiclang. raw_data is cleaned manually (or with a small script - **align.py**) to align the data. Using **cleaning.py**, the data is finally processed to remove duplicates and data from other languages (especially separating English data from Indic data)


<!-- Task 2 -->
Input directory: **raw_data_new**  (It contains the output of Task 1 post processing)
Output directory: **raw_data_new** 
It does the following tasks:
1. Cleaning - Remove duplicates, remove data from other languages, remove data that is numeric or of length less than 2 characters.
2. Language detection - Done only for languages supported by fasttext-langdetect

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

|No. |language_code|bleu_indicTrans   |chrf_indicTrans   |bleu_helsinki     |chrf_helsinki     |
|------|-------------|------------------|------------------|------------------|------------------|
|0     |bn           |40.361451397114195|67.29100086720587 |15.008718294521943|38.459893968335855|
|1     |gu           |40.09242647814781 |62.38047934152201 |17.519435117029424|41.67385242030943 |
|2     |hi           |35.46963979966534 |61.12925209053163 |11.225427865557949|38.59222728367872 |
|3     |kn           |32.147355804677694|56.59004522220443 |15.618151502462212|38.06799170855191 |
|4     |ml           |37.8225649633747  |61.7368338997521  |15.2814778557767  |39.55520687508669 |
|5     |mr           |36.618912232159545|61.060112673233135|15.732443365648534|40.030517925746025|
|6     |or           |40.61712977226381 |64.53967600298299 |11.310679447675124|36.57590226441299 |
|7     |pa           |33.19827639988097 |56.28109096317498 |16.424478002794018|40.2022064113979  |
|8     |ta           |32.618353590741094|55.570154385196666|14.990324396869909|38.452540317035634|
|9     |te           |39.97781730506786 |62.885759163173674|20.18320840530373 |43.50483959356902 |






