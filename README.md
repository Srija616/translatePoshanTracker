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
The project scrapes the data from [PoshanTracker] (https://www.poshantracker.in/) website to create a parallel dataset of English-Indic language format. The Indic language data is then translated to English using two different models - [indicTrans] () and [Helsinki] (). Finally, the BLEU scores and CHRF scores are calculated.

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
 3. For task 2 and 3, indic-nlp library and indicTrans translation model is required, so run the script.sh file
 ```sh
   bash script.sh
   ```
   In case you are in Windows environment and want to run the script from VS Code: 

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


0,bn,bn
1,gu,gu
2,hi,hi
3,kn,kn
4,ml,ml
5,mr,mr
6,or,or
7,pa,pa
8,ta,ta
9,te,te
10,as,as
11,brx,en
12,doi,en
13,kok,mr
14,mai,hi
15,mni,bn
16,ne,ne
17,sat,en
18,sd,hi
19,ur,ur


<!-- Task 3 -->
## Task 3

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Task 4 -->
## Task 4

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

