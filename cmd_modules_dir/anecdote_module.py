import re

import requests
from bs4 import BeautifulSoup
# from lxml import html


def get_anecdote_html_page():
    url = 'http://www.trees-and-lambdas.info/matushansky/stirlitz.html'
    r = requests.get(url)
    return r.text


def parse_anecdote_data(text):
    soup = BeautifulSoup(text, features='lxml')
    anecdote_list = soup.find_all('p')
    parsed_list = []
    pattern = re.compile('>[\na-zA-Zа-яА-Я0-9/\\\,\.\-?!": ]+<')
    for anecdote in anecdote_list:
        anecdote = str(anecdote).replace('\r\n', '').replace('<br/>', '<br/>\n')
        clean_list = re.findall(pattern, anecdote)
        parsed_list.append(''.join(clean_list).replace('<', '').replace('>', ''))
    parsed_list.pop()
    parsed_list.pop(0)
    return parsed_list


def create_anecdote_list():
    data = get_anecdote_html_page()
    anecdote_list = parse_anecdote_data(data)
    return anecdote_list
