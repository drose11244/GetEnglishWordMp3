#! python3
# coding=UTF-8
import requests
import bs4
import csv


# def main():

def get_explain(word):
    # https://curl.trillworks.com/ <= It's good websit can tranlate bash curl to python format
    cookies = {
        'XSRF-TOKEN': 'd8212e83-98e4-4a7c-b5d5-a74e3824923f',
        'amp-access': 'amp-XaQphVk46Ug6CLyhJYoxBg',
        'preferredDictionaries': 'english-chinese-traditional,english-chinese-simplified,english,british-grammar',
        '_ga': 'GA1.3.2124830091.1573182452',
        '_gid': 'GA1.3.1171566713.1573182452',
        '_gat': '1',
        '_fbp': 'fb.1.1573182452379.1914471282',
        '__gads': 'ID=19307f7324460004:T=1573182448:S=ALNI_MbXZc4DuuIUjHXrnZmdR0HNknlqwg',
        'cto_lwid': '2ffd11ae-7825-48d6-bf81-212f6b90215d',
        'cto_bundle': 'c-vKWV83RzQxUUIyRU0zeE1kVFhaUFluZ1JtMWIlMkZPcHByVDdDelYzRlklMkZOenIlMkZTdDRGUWZBOGxBSHclMkJ3UkpiZHRYQ1VYdURVNFVZdVBwY2ZUVHNOUWpyN1Q4UnhxaXJ6OFEwU0R2TUtkUldCajMxQkFubld6S3VITkN1YU1Mck1ibTBUTTlmbmZYYyUyQjVlVnk5d1pGemxXNEFnJTNEJTNE',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0',
        'Accept': 'audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/acrobatic',
        'Range': 'bytes=0-',
        'Connection': 'keep-alive',
    }

    # url = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/courier'
    # url = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/turkish?q=Turkish'
    # print("input search word ")
    # search_word = input()

    get_value ={}
    get_Total=''
    search_word = word
    dict_url_header = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'
    dict_url = dict_url_header+search_word

    response = requests.get(dict_url, headers=headers, cookies=cookies)
    getResult = bs4.BeautifulSoup(response.text)

    # Word
    getWord = getResult.findAll('div', class_='di-title')
    getWord = getWord[1].text.strip()
    get_value['Word'] = getWord

    # print("")
    # print(getWord)
    # print("")


    #音標 Phonetic symbol
    get_phonetic_symbol = getResult.findAll('span', class_='ipa dipa lpr-2 lpl-1')
    phonetic_symbol = '/'+get_phonetic_symbol[0].text.strip()+'/'
    get_value['PhoneticSymol'] = phonetic_symbol
    # get_value['PhoneticSymbol':phonetic_symbol]
    # print(phonetic_symbol)
    # print("")
    

    # get part of speech
    get_part_of_speech_amount = getResult.find_all('div',class_='pr entry-body__el')
    len_part_od_speech = len(get_part_of_speech_amount)
    for pos in range(0,len_part_od_speech):

        # part of speech
        get_part_Of_speech = getResult.findAll('span', class_='pos dpos')
        get_part_of_speech_text = get_part_Of_speech[pos].text.strip()
        get_value['PartOfSpeech'] = get_part_of_speech_text
        # print(get_part_of_speech_text)

        # Explain => def-block ddef_block
        get_explain = get_part_of_speech_amount[pos].find_all('div',class_='def-block ddef_block')
        let_explain = len(get_explain)
        for explain in range(0,let_explain):

            # English
            get_explain_English = get_explain[explain].find('div', class_='def ddef_d db')
            explain_English = get_explain_English.text.strip()
            # get_value['Explain'] = explain_English
            explain_English = "<div>"+explain_English+"<div>"
            get_Total = explain_English + get_Total
            # print("<div>"+explain_English+"<div>")

            # Mandarin
            get_explain_Mandarin = get_explain[explain].find('span', class_='trans dtrans dtrans-se')
            explain_Mandarin = get_explain_Mandarin.text.strip()
            explain_Mandarin = "<div>"+explain_Mandarin+"<div>"
            get_Total = explain_Mandarin + get_Total
            get_value['Explain'] = get_Total
            # explain_Mandarin = get_explain_Mandarin.text.strip()
            # get_Total = explain_Mandarin + get_Total

            # print(explain_Mandarin)
            # print("<div>"+explain_Mandarin+"<div>")
            # print("")

            # Next time work to add example in explain
            # if getExplain_In_block[1].find('div',class_='examp dexamp'):
            #     print("yes")
            # else:
            #     print('no')
    

            return get_value


# if __name__== "__main__":
#     main()