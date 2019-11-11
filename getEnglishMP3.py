#! python3
# coding=UTF-8
import requests
from urllib.parse import urlparse
import packages.cookieAndheaders as cookieAndheaders
import sys
import bs4
import os


def basename(url):
    get_Position = url.rfind('/') + 1
    return url[get_Position:]

def main():

    while(1):
        try:
            # dict_url = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/hello'
            print("input search word ")
            search_word = input()
            dict_url_header = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'
            dict_url = dict_url_header+search_word
            
            get_dict_information = requests.get(dict_url, headers=cookieAndheaders.headers, cookies=cookieAndheaders.cookies)
            getResult = bs4.BeautifulSoup(get_dict_information.text)
            allData = getResult.findAll('source')
            websit_mp3_header = 'https://dictionary.cambridge.org'
            get_dict_websit_mp3 = str(websit_mp3_header)+allData[2]['src']
            # print("Input your URL: ")
            # url = input()
            url = get_dict_websit_mp3
            response = requests.get(url, headers=cookieAndheaders.headers, cookies=cookieAndheaders.cookies)

            # filen_information = urlparse(url)
            # url_path = filen_information.path
            get_basename = search_word+".mp3"
            folder = 'voices/'
            if not os.path.exists(folder):
                os.makedirs(folder)
                print("builded folder")
            
            path = folder +str(get_basename)
            with open(path,'wb') as f:
                f.write(response.content)
                print("")
                print("get it")
                print("")
                
        except KeyboardInterrupt:
            print ("")
            print ("Bye")
            sys.exit()

        except:
            print("")
            print("Downlaod has error")
            # pass



if __name__== "__main__":
    main()