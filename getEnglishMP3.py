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


    # https://curl.trillworks.com/ <= It's good websit can tranlate bash curl to python format
    # cookies = {
    #     'XSRF-TOKEN': 'd8212e83-98e4-4a7c-b5d5-a74e3824923f',
    #     'amp-access': 'amp-XaQphVk46Ug6CLyhJYoxBg',
    #     'preferredDictionaries': 'english-chinese-traditional,english-chinese-simplified,english,british-grammar',
    #     '_ga': 'GA1.3.2124830091.1573182452',
    #     '_gid': 'GA1.3.1171566713.1573182452',
    #     '_gat': '1',
    #     '_fbp': 'fb.1.1573182452379.1914471282',
    #     '__gads': 'ID=19307f7324460004:T=1573182448:S=ALNI_MbXZc4DuuIUjHXrnZmdR0HNknlqwg',
    #     'cto_lwid': '2ffd11ae-7825-48d6-bf81-212f6b90215d',
    #     'cto_bundle': 'c-vKWV83RzQxUUIyRU0zeE1kVFhaUFluZ1JtMWIlMkZPcHByVDdDelYzRlklMkZOenIlMkZTdDRGUWZBOGxBSHclMkJ3UkpiZHRYQ1VYdURVNFVZdVBwY2ZUVHNOUWpyN1Q4UnhxaXJ6OFEwU0R2TUtkUldCajMxQkFubld6S3VITkN1YU1Mck1ibTBUTTlmbmZYYyUyQjVlVnk5d1pGemxXNEFnJTNEJTNE',
    # }

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0',
    #     'Accept': 'audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5',
    #     'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    #     'Referer': 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/acrobatic',
    #     'Range': 'bytes=0-',
    #     'Connection': 'keep-alive',
    # }

    

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