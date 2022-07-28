import re
from bs4 import BeautifulSoup
# from lxml import html
# import requests


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
