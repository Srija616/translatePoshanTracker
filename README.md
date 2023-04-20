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
The project scrapes the data from [PoshanTracker] (https://www.poshantracker.in/) website to create a parallel dataset of English-Indic language format. The Indic language data is then translated to English using two different models - [indicTrans] () and [Helsinki] (). Finally, the BLEU scores and CHRF scores are calculated. The five tasks and the instructions to run the code are described in section A and section B respectively. 

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

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


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

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
  
  ### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Task 1 -->
## Downloading the data

After installing the requirements, run the web_scraper.py file. The web_scraper.py module extracts data from [PoshanTracker] (https://www.poshantracker.in/) and its internally linked webpages.
The extracted data is divided into three sets:
1. Data stored in rawBinaryData - it consists of csv files in the format en-indiclang. rawBinaryData is cleaned manually (or with a small script) to align the data. Using cleaning.py, the data is finally processed to remove duplicates and data from other languages (especially separating English data from Indic data)


<!-- Task 2 -->
## Task 2

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

