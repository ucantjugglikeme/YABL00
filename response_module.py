import re


def get_response_dict():
    kw_file = open(file='../YABL00_DATABASE/text_to_answer', encoding='utf-8')
    # kw_dict = {re.split('\|', line)[0]: re.split('\|', line)[1] for line in kw_file}
    # kw_dict = {re.split('\|', line)[0]: [val for val in re.split('\|', line)[1].split(';')] for line in kw_file}
    kw_dict = {
        re.split('\|', line.rstrip('\n'))[0]: {
            re.split('->', val)[0]: re.split('->', val)[1].replace('\\n', '\n')
            for val in re.split('\|', line.rstrip('\n'))[1].split(';')
        }
        for line in kw_file
    }
    kw_file.close()
    return kw_dict


def get_response_if_kw(msg):
    kw_dict = get_response_dict()
    for key, value in kw_dict.items():
        if re.fullmatch(key, msg):
            return value
    return None
