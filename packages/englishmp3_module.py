#! python3
# coding=UTF-8
import requests
import sys
import bs4
import os
import packages.tools as tools

def func_EnglishMp3(word):
    try:
        search_word = word
        dict_url = tools.dictitionaryHeaders + search_word

        get_dict_information = requests.get(
            dict_url, headers=tools.headers, cookies=tools.cookies)
        get_Result = bs4.BeautifulSoup(get_dict_information.text, 'html.parser')
        get_Word = get_Result.findAll('div', class_='di-title')
        if not get_Word:
            print("Not found.")
            return 0
        get_Word = get_Word[1].text.strip()
        
        allData = get_Result.findAll('source')
        websit_mp3_header = 'https://dictionary.cambridge.org'
        get_dict_websit_mp3 = str(websit_mp3_header)+allData[2]['src']
        mp3_url = get_dict_websit_mp3
        response = requests.get(
            mp3_url, headers=tools.headers, cookies=tools.cookies)

        file_mp3 = get_Word+".mp3"
        folder = 'voices/'
        if not os.path.exists(folder):
            os.makedirs(folder)
            print("音檔資料已建立\n")

        path = folder + str(file_mp3)
        with open(path, 'wb') as f:
            f.write(response.content)
            print( file_mp3 +" 音檔已下載\n" )

    except KeyboardInterrupt:
        print("Bye ~ ~")
        sys.exit()

    except:
        print("EnglishMp3_Unexpected error:", sys.exc_info()[0])
