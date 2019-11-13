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
import packages.tools as tools



def main():
    try:
        with open('input.txt', "r", encoding='utf-8') as input_target:
            
            get_input_txt = input_target.read()
            get_keyword = get_input_txt.split("\n")
            len_keyword = len(get_keyword)

            
            filename = tools.fun_date()+".csv"
            folderName = 'OutputCSV/'
            folderPath = folderName + filename
            for i in range(0, len_keyword):
                input_Word = get_keyword[i]
                get_explain = explain_module.fun_Explain(input_Word)

                if get_explain:
                    # Get vocabulary
                    WORD = get_explain['Word']
                    POS = get_explain['PhoneticSymol']
                    VOICES = '[sound:'+input_Word+'.mp3]'
                    EXPLAIN = get_explain['Explain']

                    # print(get_explain['Word'])
                    # print(get_explain['PhoneticSymol'])
                    # print(get_explain['PartOfSpeech'])
                    # print(get_explain['Explain'])

                    if not os.path.exists(folderName):
                        os.makedirs(folderName)
                        print("Output/CSV 已建立資料夾\n")

                    with open(folderPath, 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([WORD, POS, VOICES, EXPLAIN])
                        print(str(WORD) + ' 已寫入CSV檔案\n')
                        englishmp3_module.func_EnglishMp3(input_Word)

                else:

                    if input_Word == '':
                        print("only space.")
                        return

                    err_namePath = 'error_'+filename
                    err_folderPath = 'OutputCSV/'+err_namePath
                    try:
                        with open(err_folderPath, 'a', encoding='utf-8') as write_file:
                            text = input_Word+'\n'
                            write_file.write(text)
                    except:
                        print("error_csv_Unexpected error:", sys.exc_info()[0])

    except KeyboardInterrupt:
        print("Bye ~ ~")
        sys.exit()

    except:
        print("make_Unexpected error:", sys.exc_info()[0])
        input_files = 'input.txt'
        if not os.path.isfile(input_files):
            print("請確認 input.txt 是否存在，且檔案中至少需要一筆資料。")
            with open(input_files, "a", encoding='utf-8') as input_target:
                input_target.write('hello\n')
                input_target.write('world\n')
                print("已生產input.txt\n")
    finally:
        print('完成\n')


if __name__ == "__main__":
    main()
