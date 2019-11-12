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
    get_phonetic_symbol = getResult.find_all('span', class_='ipa dipa lpr-2 lpl-1')
    phonetic_symbol = '/'+get_phonetic_symbol[0].text.strip()+'/'
    get_value['PhoneticSymol'] = phonetic_symbol
    # print(phonetic_symbol)
    # print("")

    # get part of speech
    get_part_of_speech_amount = getResult.find_all('div',class_='pr entry-body__el')
    len_part_od_speech = len(get_part_of_speech_amount)

    for position_part_of_speech in range(0,len_part_od_speech):
        # part of speech
        get_part_Of_speech = getResult.find_all('span', class_='pos dpos')
        get_part_of_speech_text = get_part_Of_speech[position_part_of_speech].text.strip()
        # get_value['PartOfSpeech'] = get_part_of_speech_text
        part_of_speech = "<div>"+get_part_of_speech_text+"</div>"
        get_Total += part_of_speech
        # print(get_part_of_speech_text)

        ## Explain => def-block ddef_block
        get_explain = get_part_of_speech_amount[position_part_of_speech].find_all('div',class_='def-block ddef_block')
        let_explain = len(get_explain)

        for explain in range(0,let_explain):

            # English => ddef_h
            get_explain_English = get_explain[explain].find_all('div', class_='def ddef_d db')
            len_get_explain_English = len(get_explain_English)
            for position_explain_in_Enghish in range(0,len_get_explain_English):
                get_explain_English = get_explain_English[position_explain_in_Enghish]
                explain_English = get_explain_English.text
                explain_English = "<div>"+explain_English+"</div>"
                get_Total += explain_English
                # print(explain_English)

            # Mandarin => def-body ddef_b
            get_explain_Mandarin = get_explain[explain].find_all('span', class_='trans dtrans dtrans-se')
            len_get_explain_Mandarin = len(get_explain_Mandarin)
            for Position_explain_in_Mandarin in range(0,len_get_explain_Mandarin):
                get_explain_Mandarin = get_explain_Mandarin[Position_explain_in_Mandarin]
                explain_Mandarin = get_explain_Mandarin.text
                explain_Mandarin = "<div>"+explain_Mandarin+"</div>"
                get_Total += explain_Mandarin
                # print(explain_Mandarin)

                get_example_English = get_explain[explain].find_all('span', class_='eg deg')
                get_example_Mandarin = get_explain[explain].find_all('span', class_='trans dtrans dtrans-se hdb')
                let_example = len(get_example_English)

                for pos_example in range(0,let_example):

                    example_English = get_example_English[pos_example].text
                    example_English = "<div>"+example_English+"</div>"
                    get_Total += example_English

                    example_Mandarin = get_example_Mandarin[pos_example].text
                    example_Mandarin = "<div>"+example_Mandarin+"</div>"
                    get_Total += example_Mandarin
                    
                    # print(example_English)
                    # print(example_Mandarin)

    example_Mandarin = "<a href=\""+ dict_url +"\" >More...</a>"
    get_Total += example_Mandarin
    get_value['Explain'] = get_Total

    print(get_value)
    print("")

    return get_value