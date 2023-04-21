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