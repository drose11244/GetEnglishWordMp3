#! python3
# coding=UTF-8
import requests
import sys
import bs4
import os
import packages.cookieAndheaders as cookieAndheaders
from urllib.parse import urlparse

def basename(url):
    get_Position = url.rfind('/') + 1
    return url[get_Position:]

def getEnglishMp3(word):
    search_word = word
    dict_url_header = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'
    dict_url = dict_url_header+search_word
    
    get_dict_information = requests.get(dict_url, headers=cookieAndheaders.headers, cookies=cookieAndheaders.cookies)
    getResult = bs4.BeautifulSoup(get_dict_information.text,'html.parser')
    allData = getResult.findAll('source')
    websit_mp3_header = 'https://dictionary.cambridge.org'
    get_dict_websit_mp3 = str(websit_mp3_header)+allData[2]['src']
    url = get_dict_websit_mp3
    response = requests.get(url, headers=cookieAndheaders.headers, cookies=cookieAndheaders.cookies)

    get_basename = search_word+".mp3"
    folder = 'voices/'
    if not os.path.exists(folder):
        os.makedirs(folder)
        # print("builded folder")
        print("音檔資料已建立")
    
    path = folder +str(get_basename)
    with open(path,'wb') as f:
        f.write(response.content)
        print("")
        # print("Voives get it")
        print(get_basename+" 音檔已下載")
        print("")
