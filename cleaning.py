# run this file only after aligning data - by modifying the script in align.py
# To run this file, your data must be aligned, i.e. in each row the Indic sentence should be a translation of the English sentence

import pandas as pd
from ftlangdetect import detect
import utils
import os
import config

# for marking purposes: use the directory abc which has aligned but unclean data
# NOTE: splitting is performed as part of web scraping itself.
lang_detected = []
directory = config.raw_data_new_directory
save_directory = "raw_temp"
directory_unsupported = 'cleanUnsupported'

for file in os.listdir(directory):
    language_code = file[3:-4]  # en_hi.csv format of files
    print (f"Processing for {language_code}")
    df = pd.read_csv(os.path.join(directory, file), encoding = 'utf-8')
    df.drop_duplicates(inplace=True) 
    count = df[df.columns[1]].count()
    new_df = []
    # only include in data if English text is not present in Indic language column, data is not specifically numeric and length of data is more than 2
    for index, row in df.iterrows():
        try:
            if detect(row[language_code])['lang'] != "en" and row[language_code].isnumeric() == False and row['en'].isnumeric() == False and len(row['en']) >=2 :
                new_row = row.to_list()
                new_df.append(new_row)
        except:
            print ("exception occurred")
            continue
    text_string = ' '.join([str(elem) for elem in new_df])
    detected_language = utils.detect_language(text_string)  # fix this line
    lang_detected.append([language_code, detected_language])
    print (F"language_code: {language_code}, count_new: {len(new_df)}, count_old: {count}")
    new_df = pd.DataFrame(new_df, columns=["en", language_code])
    new_df.to_csv(os.path.join(save_directory , file), index= False)


for file in (os.listdir(directory_unsupported)):
    language_code = file[:-4]
    print (f"Processing for: {language_code}")
    df = pd.read_csv(os.path.join(directory_unsupported, file), encoding = 'utf-8')
    new_df = df["data"].to_list()
    text_string = ' '.join([str(elem) for elem in new_df[:100]])
    detected_language = utils.detect_language(text_string)  # fix this line
    lang_detected.append([language_code, detected_language])
    
dictionary_lang_deteced = pd.DataFrame(lang_detected, columns = ["original_language", "detected_langauge"])
dictionary_lang_deteced.to_csv("language_detected.csv")