import pandas as pd
from ftlangdetect import detect

directory = "rawBinaryData"
import os
for file in os.listdir(directory):
    language_code = file[3:]
    language_code = language_code[:-4]
    df = pd.read_csv(os.path.join(directory, file), encoding = 'utf-8')
    df.drop_duplicates(inplace=True)
    count = df[df.columns[1]].count()
    new_df = []
    for index, row in df.iterrows():
        try:
            if detect(row[language_code])['lang'] != "en" and row[language_code].isnumeric() == False and row['en'].isnumeric() == False:
                new_row = row.to_list()
                new_df.append(new_row)
        except:
            print ("exception occurred")
            continue
    print (F"language_code: {language_code}, count_new: {len(new_df)}, count_old: {count}")
    new_df = pd.DataFrame(new_df, columns=["en", language_code])
    new_df.to_csv(file, index= False)
            

# df = pd.read_csv("en_or.csv")
# count = df[df.columns[1]].count()
# for i in range(214, count-1):
#     df.loc[i, "en"] = df.loc[i+1, "en"]
# df.to_csv("en_or.csv", index=False)