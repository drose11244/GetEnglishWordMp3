#! python3
# coding=UTF-8
import requests
import bs4
import csv
import os 
import sys
import datetime
import packages.explain_module as explain_module
import packages.englishmp3_module as englishmp3_module



def main():
    try:
        with open('input.txt', "r", encoding='utf-8') as input_target:
            get_input_txt = input_target.read()
            get_keyword = get_input_txt.split("\n")
            len_keyword = len(get_keyword)
            time = datetime.datetime.now()
            year = time.year
            month = time.month
            day = time.day
            hour = time.hour
            mins = time.minute
            second = time.second
            getTimeNow = str(year) + str(month) + str(day) + \
                str(hour) + str(mins) + str(second)
            filename = str(getTimeNow) + ".csv"

            folderName = 'OutputCSV/'
            folderPath = folderName + filename
            for i in range(0,len_keyword):
                ## csv file output
                inputWord = get_keyword[i]
                get_explain = explain_module.get_explain(inputWord)
                
                if get_explain:
                    WORD = get_explain['Word']
                    POS = get_explain['PhoneticSymol']
                    VOICES = '[sound:'+inputWord+'.mp3]'
                    EXPLAIN =  get_explain['Explain']

                    # print(get_explain['Word'])
                    # print(get_explain['PhoneticSymol'])
                    # print(get_explain['PartOfSpeech'])
                    # print(get_explain['Explain'])

                    try:

                        if not os.path.exists(folderName):
                            os.makedirs(folderName)
                            # print("builded folder")
                            print("Output/CSV 已建立資料夾")
                        
                        with open(folderPath, 'a', newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow([WORD, POS, VOICES, EXPLAIN])
                            print(str(WORD) + ' 已寫入CSV檔案')
                            englishmp3_module.getEnglishMp3(inputWord)
                    except:
                        # print("Output has error.")
                        pass
    except:
        # print("read file and write file has  error.")
        print("請確認 input.txt 是否存在，且檔案中至少需要一筆資料。")




if __name__== "__main__":
    main()