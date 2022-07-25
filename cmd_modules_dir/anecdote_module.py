import requests
from bs4 import BeautifulSoup
# from lxml import html


def get_anecdote_html_page():
    url = 'http://www.trees-and-lambdas.info/matushansky/stirlitz.html'
    r = requests.get(url)
    # print(r.text.encode('cp1251'))
    return r.text


def parse_data(text):
    soup = BeautifulSoup(text, features='lxml')
    anecdote = soup.find('p')
    print(anecdote)


def create_anecdote_list():
    data = get_anecdote_html_page()
    parse_data(data)
    return list()
