#! python3
# coding=UTF-8
import requests
import bs4
import csv
# import explain
import explain_module
import englishmp3_module


def main():
    # 開啟輸出的 CSV 檔案
    inputWord = 'plant'
    get_explain = explain_module.get_explain(inputWord)
    WORD = get_explain['Word']
    POS = get_explain['PhoneticSymol']
    VOICES = '[sound:'+inputWord+'.mp3]'
    EXPLAIN =  get_explain['Explain']


    # print(get_explain['Word'])
    # print(get_explain['PhoneticSymol'])
    # print(get_explain['PartOfSpeech'])
    # print(get_explain['Explain'])

    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([WORD, POS, VOICES, EXPLAIN])
        englishmp3_module.getEnglishMp3(inputWord)






if __name__== "__main__":
    main()