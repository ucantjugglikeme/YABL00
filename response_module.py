import re
import cmd_modules_dir.anecdote_module as a_module


def get_response_dict():
    kw_file = open(file='../YABL00_DATABASE/text_msgs_to_answer', encoding='utf-8')
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


def get_response_if_cmd(msg, group_id):
    bot_summoning = f'(\[club{group_id}\|@yab_loo\]|Y|y)'
    if re.match(f'{bot_summoning} g a', msg):
        a_module.create_anecdote_list()
