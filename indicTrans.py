from mosestokenizer import *
import pandas as pd
import os
import time
main_path = os.getcwd()
path_dir=os.getcwd() +'\indicTrans'
os.chdir(path_dir)
from indicTrans.inference.engine import Model
indic2en_model = Model(expdir='../indic-en')

max_processing = {} # language and the dataframe max length to be processed - depending on the point where the mapping is correct

os.chdir(main_path)

directory = 'raw_data_new'
for file in os.listdir(directory):
    language_code = file[3:]
    language_code = language_code[:-4]
    print (language_code)
    df = pd.read_csv(os.path.join(directory, file), encoding = 'utf-8')
    data_to_translate = df[language_code].tolist()
    start_time = time.time()
    try:
        output = indic2en_model.batch_translate(data_to_translate, language_code, 'en')
       
        df_translated = pd.DataFrame(output, columns = ["translated"])
        df_final = pd.concat([df, df_translated], axis = 1)
        new_file = "translated_indicTrans/" + language_code + ".csv"
        df_final.to_csv(new_file, index = False)
    except:
        print (f"Language code: {language_code} translation failed")
    print (f"Time elapsed: translate: {time.time() - start_time}")

    
    
    
    
    
# df = pd.read_csv('en_hi.csv', encoding = 'utf-8')
# df_en = df.drop(['hi'], axis = 1)
# data_to_translate = df['hi'].tolist()


# output = indic2en_model.batch_translate(data_to_translate, 'hi', 'en')
# df_translated = pd.DataFrame(output)

# df_final = pd.concat([df_en, df_translated], axis = 1)
# new_file = "translated_hi_en.csv"
# df_final.to_csv(new_file)

# df.to_csv(new_file)
# # CHNAGE - the method of getting language code for each file
# language_code = file[7:]
# language_code = language_code[:-4]
# path = './' + directory + "/" + file  # CHANGE - agnostic
# print (path)
# if (language_code in INDIC):
#     # CHANGE - use read_csv
#     # sentence_batch = pd.read_csv(path, delimiter = '\n', encoding = 'utf-8') 
#     # print (sentence_batch)
#     print (f"Language : {language_code}")
#     start = time.time()
#     with open(path, 'r', encoding= 'utf-8') as f:
#         text = f.read()
#         data = text.split('\n')
#     print (data)
#     # print (f"Reading time : {time.time() - start}")
#     # sentence_batch = split_sentences(text, language_code)
#     # print (f"Time elapsed: split_sentences: {time.time() - start}")
#     sentence_batch_df = pd.DataFrame(data)
#     input_file = "indic_" + language_code + ".csv"
#     sentence_batch_df.to_csv(input_file)
#     output = indic2en_model.batch_translate(data, language_code, 'en')
#     print (f"Time elapsed: translate: {time.time() - start}")
#     df = pd.DataFrame(output)
#     new_file = "translated_" + language_code + ".csv"
#     df.to_csv(new_file)