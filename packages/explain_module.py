#! python3
# coding=UTF-8
import requests
import bs4
import csv
import sys
import packages.tools as tools


def fun_Explain(word):
    try:
        get_value = {}
        get_Total = ''
        search_word = word
        dict_url = tools.dictitionaryHeaders + search_word
        response = requests.get(
            dict_url, headers=tools.headers, cookies=tools.cookies)
        getResult = bs4.BeautifulSoup(response.text, "html.parser")

        # vocabulary
        get_Word = getResult.findAll('div', class_='di-title')

        if not get_Word:
            # Not Found Word.
            print("Not Found.\n")
            return 0

        get_Word = get_Word[1].text.strip()
        get_value['Word'] = get_Word
        # print("")
        # print(get_Word)
        # print("")

        # Phonetic symbol
        get_phonetic_symbol = getResult.find_all(
            'span', class_='ipa dipa lpr-2 lpl-1')
        phonetic_symbol = '/'+get_phonetic_symbol[0].text.strip()+'/'
        get_value['PhoneticSymol'] = phonetic_symbol
        # print(phonetic_symbol)
        # print("")

        # get part of speech
        get_part_of_speech_amount = getResult.find_all('div', class_='pr entry-body__el')
        len_part_of_speech = len(get_part_of_speech_amount)
        for position_part_of_speech in range(0, len_part_of_speech):
            get_part_Of_speech = getResult.find_all('span', class_='pos dpos')
            get_part_of_speech_text = get_part_Of_speech[position_part_of_speech].text.strip()
            part_of_explain = get_part_of_speech_text
            part_of_explain = "<div>"+part_of_explain+"</div>"
            get_Total += part_of_explain

            # Yellow line Explain => def-block ddef_block
            get_explain = get_part_of_speech_amount[position_part_of_speech].find_all(
                'div', class_='def-block ddef_block')

            # Explain
            let_explain = len(get_explain)
            for explain in range(0, let_explain):

                # English => def ddef_d db
                get_explain_English = get_explain[explain].find_all(
                    'div', class_='def ddef_d db')
                len_get_explain_English = len(get_explain_English)

                for position_explain_in_Enghish in range(0, len_get_explain_English):
                    get_explain_English = get_explain_English[position_explain_in_Enghish]
                    explain_English = get_explain_English.text
                    explain_English = "<div>"+explain_English+"</div>"
                    get_Total += explain_English
                    # print(explain_English)

                # Mandarin => trans dtrans dtrans-se
                get_explain_Mandarin = get_explain[explain].find_all(
                    'span', class_='trans dtrans dtrans-se')
                len_get_explain_Mandarin = len(get_explain_Mandarin)
                for Position_explain_in_Mandarin in range(0, len_get_explain_Mandarin):
                    get_explain_Mandarin = get_explain_Mandarin[Position_explain_in_Mandarin]
                    explain_Mandarin = get_explain_Mandarin.text
                    explain_Mandarin = "<div>"+explain_Mandarin+"</div>"
                    get_Total += explain_Mandarin
                    # print(explain_Mandarin)

        # Link to dictionary.cambridge.org
        example_Mandarin = "<a href=\'" + dict_url + "\' >More...</a>"
        get_Total += example_Mandarin
        get_value['Explain'] = get_Total

        # print(get_value)
        return get_value

    except KeyboardInterrupt:
        print("Bye ~ ~~")
        sys.exit()

    except:
        print("Explain_Unexpected error:", sys.exc_info()[0])
