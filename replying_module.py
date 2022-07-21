import rand_module


def send_msg_to_user(vk, user_id, reply_msg):
    vk.method(
        'messages.send',
        {'user_id': user_id, 'message': reply_msg, 'random_id': rand_module.get_random_id()}
    )


def send_msg_to_chat(vk, chat_id, reply_msg):
    vk.method(
        'messages.send',
        {'chat_id': chat_id, 'message': reply_msg, 'random_id': rand_module.get_random_id()}
    )
