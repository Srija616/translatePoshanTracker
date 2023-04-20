from ftlangdetect import detect
import indicnlp
from indicnlp.tokenize import sentence_tokenize
import pandas as pd
import warnings
warnings.filterwarnings("ignore") 

# most probably not required
def tokenizeSentencewise(text, language):
    # text = '\n'.join(text_list)
    data = indicnlp.tokenize.sentence_tokenize.sentence_split(text, language)
    final_data = []
    for line in data:
        lines_split = line.split('\n')
        final_data.extend(lines_split)
    return final_data

def removeOtherLanguages(text_list, language):
    final_data = []
    if (text_list == None): 
        return []
    for line in text_list:
        try:
            detected_lang = detect(line)['lang'] == language
            # the below condition helps in better scraping of data since the language detection is not 100% accurate for sindhi, maithili and oriya
            if detected_lang or (language in ['sd', 'mai'] and detected_lang == 'hi') or (language == 'or' and detected_lang== 'bn'):
                final_data.append(line) 
        except:
            continue
    return final_data

def cleanData(text_list):
    df = pd.DataFrame(text_list, columns=["text"])
    df = df[~df["text"].str.isnumeric() & (df["text"].str.len() >= 2)]
    return df["text"].tolist()
            
def detectLanguage(text):
    language_detected = ""
    language_detected = detect(text,  low_memory=False)['lang']
    return language_detected
