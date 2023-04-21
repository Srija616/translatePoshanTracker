import pandas as pd
from sacrebleu.metrics import BLEU, CHRF
import os
import multiprocessing
indic_trans_bleu = {}
indic_trans_chrf = {}
bleu = BLEU()
chrf = CHRF()

def getScore(args):
    file, directory, language_code, translated_key, english_key = args
    df = pd.read_csv(os.path.join(directory, file))
    reference = [[text.replace('\n', ' ') for text in df[english_key].to_list()]]
    machine_translated = [text.replace('\n', ' ') for text in df[translated_key].to_list()]
    bleu_score = bleu.corpus_score(machine_translated,reference)
    chrf_score = chrf.corpus_score(machine_translated,reference)
    return [language_code, bleu_score.score, chrf_score.score]

if __name__ == "__main__":
    num_processes = min(os.cpu_count(), 2)
    directory_indic = 'translated_indicTrans'
    directory_helsinki = 'translated_helsinki'
    scores_indicTrans = []
    scores_helsinki = []
    with multiprocessing.Pool(processes=num_processes) as pool:
        scores_indicTrans = pool.map(getScore, [(file, directory_indic, file[:-4], "translated", "en") for file in os.listdir(directory_indic)]) #get all data from websites.
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        scores_helsinki = pool.map(getScore, [(file, directory_helsinki, file[:-4], "translated_helsinki", "en") for file in os.listdir(directory_helsinki)])
    
    df_indicTrans = pd.DataFrame(scores_indicTrans, columns = ["language_code", "bleu_indicTrans", "chrf_indicTrans"])
    df_helsinki = pd.DataFrame(scores_helsinki, columns = ["language_code", "bleu_helsinki", "chrf_helsinki"])
    df = pd.merge(df_indicTrans, df_helsinki, on = "language_code", how = "outer")
    df.to_csv("scores.csv")
   