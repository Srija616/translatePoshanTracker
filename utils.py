from ftlangdetect import detect
import indicnlp
from indicnlp.tokenize import sentence_tokenize
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
    final_data = []
    # can be optimized using pandas df
    for i in text_list:
        if i.isnumeric() or len(i) <2:
            continue
        else:
            final_data.append(i)
    return final_data
            
def detectLanguage(text):
    language_detected = ""
    language_detected = detect(text,  low_memory=False)['lang']
    return language_detected



 
    
# # detect language
# # clean data
# # make dataframe

# # clean data
# directory = 'data'

# for filename in os.scandir(directory):
#     print (filename)
#     with open(filename, 'r', encoding= 'utf-8') as f:
#         text = f.read()
#     print (type(text))
#     print(text)
#     detected_lang = detectLanguage(text)
#     print (detected_lang)
    
#     # data = pd.read_csv(filename, delimiter = '\n', encoding = 'utf-8', names = ['text_data'])
#     # print (data.head)
#     # print (data.shape)
#     data = indicnlp.tokenize.sentence_tokenize.sentence_split(text, 'en')
#     # print ("Data", data)
#     f_data = []
#     for line in data:
#         lines_split = line.split('\n')
#         f_data.extend(lines_split)
    
#     detected_language = identify_language(f_data[0])
#     final_data = []
#     for line in f_data:
#         try:
#             # line= line.replace('"', '\\"')
#             if identify_language(line) == detected_language:
#                 final_data.append(line) 
#             else:
#                 print ("wrong lang: ", line)
#         except:
#             print ("except: ", line)
#     print (final_data)
#     print (len(final_data))
#     filename = "output_new.txt"
#     with open(filename, "w", encoding="utf-8") as f:
#             # Write the data to the file
#             f.write('\n'.join(final_data))
#             # f.write(final_data)
#     # indicnlp.tokenize.sentence_tokenize.sentence_split(final_data, 'en')
    
    
# #     mask = data.apply(lambda x: identify_language(x['text_data']) == detected_language , axis=1)
# # # use the mask to filter the original DataFrame
# #     df_filtered = data[~mask]
# #     print (df_filtered.head)
# #         # print ("full data didn't work")
#     # try:
#     #     detected_language = identify_language(data)
#     #     print ("full data worked")
#     # except:
#         # detected_language = identify_language(data.iloc[0])
#         # print ("full data didn't work")
      
        


