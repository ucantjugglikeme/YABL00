import json
import re
import urllib3
import nlpcloud
import delays
from bs4 import BeautifulSoup
# from lxml import html
import requests


def get_anecdote_html_page():
    # HOW TO GET HTML PAGE AND WRITE TO FILE:
    # url = 'http://www.trees-and-lambdas.info/matushansky/stirlitz.html'
    # r = requests.get(url)
    # with open('../YABL00_DATABASE/anecdotes.html', 'w') as output_file:
    #    output_file.write(str(r.text.encode('utf-8')))

    # HOW TO GET HTML PAGE FILE
    with open('../YABL00_DATABASE/anecdotes.html') as input_file:
        text = input_file.read()
    return text


def parse_anecdote_data(text):
    soup = BeautifulSoup(text, features='lxml')
    anecdote_list = soup.find_all('p')
    parsed_list = []
    # '>[\na-zA-Zа-яА-Я0-9/\\\,\.\-?!": ]+<'  --  earliest version (???)
    pattern = re.compile('>[^<>]+<')
    for anecdote in anecdote_list:
        anecdote = str(anecdote).replace('\\r\\n', '').replace('<br/>', '\n')
        clean_list = re.findall(pattern, anecdote)
        parsed_list.append(''.join(clean_list).replace('<', '').replace('>', '').replace('\\', ''))
    parsed_list.pop()
    parsed_list.pop(0)
    return parsed_list


def create_anecdote_list():
    data = get_anecdote_html_page()
    anecdote_list = parse_anecdote_data(data)
    return anecdote_list


# based
def get_html_page(src_url, file_name):
    # HOW TO GET HTML PAGE AND WRITE TO FILE:
    r = requests.get(src_url)
    with open(f'../YABL00_DATABASE/{file_name}.html', 'w') as output_file:
        output_file.write(str(r.text.encode('utf-8')))

    # HOW TO GET HTML PAGE FILE
    with open(f'../YABL00_DATABASE/{file_name}.html') as input_file:
        text = input_file.read()
    return text


# f*ck Google API
# all my homies use nlpcloud lib
def get_translated_data(data_dict):
    with open('../YABL00_DATABASE/nlp_token') as token_file:
        nlp_token = token_file.read()
    nlp_client = nlpcloud.Client('nllb-200-3-3b', nlp_token)

    response_list = list()
    import_replacement = ['Деятельность', 'Тип']
    for i in range(2):
        key, value = list(data_dict.items())[i]
        translated_response = nlp_client.translation(value, 'eng_Latn', 'rus_Cyrl')
        response_list.append(f'{import_replacement[i]}: '
                             f'{translated_response.get("translation_text").lower().replace(".", "")}')

    response_list.append(
        f'Участников: {data_dict.get("participants")}\nСтоимость: {data_dict.get("price")}\n'
        f'Ссылка: {data_dict.get("link")}\nКлюч: {data_dict.get("key")}\n'
        f'Доступность: {data_dict.get("accessibility")}'
    )

    translated_text = '\n'.join(response_list)
    return translated_text


def get_beaut_str(data_dict):
    beauties = list()
    for key, value in data_dict.items():
        beauties.append(
            f'{key.capitalize()}: {str(value).lower()}'
        )
    str_to_return = '\n'.join(beauties)
    return str_to_return


# another cmd
def get_activity_if_bored(ru):
    delta = delays.get_delta_activity_time()
    if delta.seconds < 45:
        return f'Подожди пожалуйста ещё {45 - delta.seconds} сек!\n' \
               f'Сервер ругается...'
    else:
        delays.update_activity_ltime()

    urllib3.disable_warnings()
    data = requests.get(
        'https://www.boredapi.com/api/activity', verify=False
    ).text
    data_decoded = json.loads(data)

    str_data = get_translated_data(data_decoded) if ru \
        else get_beaut_str(data_decoded)
    return str_data
