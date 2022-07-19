import re


def get_response_dict(splitter=':'):
    kw_file = open(file='../YABL00_DATABASE/keywords', encoding='utf-8')
    kw_dict = {re.split(splitter, line)[0]: re.split(splitter, line)[1] for line in kw_file}
    return kw_dict


def get_response_if_kw(msg):
    kw_dict = get_response_dict()
    for key, value in kw_dict.items():
        if re.fullmatch(key, msg):
            return value
    return None
