from ftlangdetect import detect
import pandas as pd
import indicnlp
from indicnlp.tokenize import sentence_tokenize
import warnings
warnings.filterwarnings("ignore") 

def split_sentences(text, language):
    ''' text(string): Text to be split
        language (string): language isocode for text
    '''
    data = indicnlp.tokenize.sentence_tokenize.sentence_split(text, language)
    final_data = [line.strip() for sentence in data for line in sentence.split('\n')]
    return final_data

def remove_other_languages(text_list, language):
    final_data = []
    if (text_list == None or len(text_list) == 0): 
        return text_list

    for line in text_list:
        try:
            detected_lang = detect(line)['lang'] == language # detecting language for each line to remove other language's data
            # the below condition helps in better scraping of data since the language detection is not 100% accurate for sindhi, maithili and oriya
            if detected_lang or (language in ['sd', 'mai'] and detected_lang == 'hi') or (language == 'or' and detected_lang== 'bn'):
                final_data.append(line) 
        except:
            continue
    return final_data

def clean_data(text_list):
    df = pd.DataFrame(text_list, columns=["text"])
    df = df[~df["text"].str.isnumeric() & (df["text"].str.len() >= 2)]
    return df["text"].tolist()
            
def detect_language(text):
    # text should not have \n characters
    text.replace("\n", "")
    language_detected = ""
    language_detected = detect(text,  low_memory=False)['lang']
    return language_detected
