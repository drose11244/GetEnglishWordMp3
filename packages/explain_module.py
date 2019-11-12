#! python3
# coding=UTF-8
import requests
import bs4
import csv
import packages.cookieAndheaders as cookieAndheaders

def get_explain(word):
    get_value ={}
    get_Total=''
    search_word = word
    dict_url_header = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'
    dict_url = dict_url_header+search_word

    response = requests.get(dict_url, headers=cookieAndheaders.headers, cookies=cookieAndheaders.cookies)
    getResult = bs4.BeautifulSoup(response.text,"html.parser")

    # Word
    getWord = getResult.findAll('div', class_='di-title')

    if not getWord:
        # Not Found Word.
        return 0

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
            explain_English = "<div>"+explain_English+"</div>"
            get_Total = explain_English + get_Total
            # print("<div>"+explain_English+"<div>")

            # Mandarin
            get_explain_Mandarin = get_explain[explain].find('span', class_='trans dtrans dtrans-se')
            explain_Mandarin = get_explain_Mandarin.text.strip()
            explain_Mandarin = "<div>"+explain_Mandarin+"</div>"
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