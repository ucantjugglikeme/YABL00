import re
import cmd_modules_dir.anecdote_module as a_module
import interaction_module
import rand_module


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


def prepare_members_data(profiles):
    users = list()
    for profile in profiles:
        user_name = f'[id{profile.get("id")}|{profile.get("first_name")} ' \
                    f'{profile.get("last_name")}]'
        users.append(user_name)
    return users


def get_response_if_who_dies(vk, msg, address_str, _id, peer_id, group_id):
    if re.match('кто сдохнет первым[ ]?[?]?', msg.lower()):
        if address_str == 'chat_id':
            serv_response = interaction_module.get_chat_info(vk, peer_id, group_id)
            profiles = serv_response['profiles']
            users_list = prepare_members_data(profiles)
            rand_member = rand_module.get_random_iterable_item(users_list)
            return f'Я думаю, что это - {rand_member}!'
        else:
            return 'Определённо не я!'
    return None


def get_response_if_anecdote(msg, group_id):
    bot_summoning = f'(\[club{group_id}\|[@]?[а-яА-Яa-zA-Z_0-9 ]+\][,]?|Y|y)'
    if re.match(f'{bot_summoning} g a', msg):
        anecdotes = a_module.create_anecdote_list()
        return rand_module.get_random_iterable_item(anecdotes)
    return None


def get_response_if_bored(msg, group_id):
    bot_summoning = f'(\[club{group_id}\|[@]?[a-zA-Z_0-9]+\][,]?|Y|y)'
    if re.match(f'{bot_summoning} I\'m bored( as fuck)?', msg):
        return a_module.get_activity_if_bored(False)
    elif re.match(f'{bot_summoning} мне скучно( жесть как)?', msg):
        return a_module.get_activity_if_bored(True)
