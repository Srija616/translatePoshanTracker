from transformers import pipeline
import pandas as pd
import os 
import time
import multiprocessing

batch_size = 32
supported_indic=['bn','hi','gu','kn', 'mr', 'ml', 'or','ta','te']

def batch_data(data, batch_size=32):
    return [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

def flatten(l):
    return [item for sublist in l for item in sublist]

directory = 'raw_data_new'
num_processes = min(os.cpu_count(), 8)  # Set the number of processes to use
print ("num_processes", num_processes)
def process_file(file):
    language_code = file[3:-4]
    if (language_code in supported_indic):
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en",batch_size=batch_size, src_lang=language_code, tgt_lang='en')
        df = pd.read_csv(os.path.join(directory, file), encoding='utf-8')
        data = df[language_code].values.tolist()
        data = batch_data(data)
        output = []
        start_time = time.time()
        for batch in data:
            output_data = translator(batch)
            out_data = [d['translation_text'] for d in output_data]
            output.extend(out_data)
            print (time.time() - start_time)
        df_translated = pd.DataFrame(output, columns=["translated_helsinki"])
        df_final = pd.concat([df, df_translated], axis=1)
        new_file = "translated_helsinki/" + language_code + ".csv"
        df_final.to_csv(new_file, index=False)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=num_processes)
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    pool.map(process_file, files)
    pool.close()
    pool.join()
         
        