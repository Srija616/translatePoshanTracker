from transformers import pipeline
import pandas as pd
import os 
import time
import multiprocessing
import config
batch_size = 32
supported_indic=['bn','hi','gu','kn', 'mr', 'ml', 'or','ta','te']

# batching is making the process slower
def batch_data(data, batch_size=32):
    return [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

directory = config.raw_data_new_directory

num_processes = min(os.cpu_count(), 8)  # Set the number of processes to use
print ("num_processes", num_processes)
def process_file(file):
    language_code = file[3:-4]
    if (language_code in supported_indic):
        print (language_code)
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en", max_length = 512, src_lang=language_code, tgt_lang='en', truncation = 'longest_first')
        df = pd.read_csv(os.path.join(directory, file), encoding='utf-8')
        
        data = df[language_code].values.tolist()
        output = []
        start_time = time.time()
        output = translator(data)
        output = [d['translation_text'] for d in output]
        print (f"Time taken for translation: {time.time() - start_time}")
        df_translated = pd.DataFrame(output, columns=["translated_helsinki"])
        df_final = pd.concat([df, df_translated], axis=1)
        new_file = "translated_helsinki/" + language_code + ".csv"
        df_final.to_csv(new_file, index=False)

if __name__ == '__main__':
    # pool = multiprocessing.Pool(processes=num_processes)
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    for file in files:
        process_file(file)
    # pool.map(process_file, files)
    # pool.close()
    # pool.join()
         
        