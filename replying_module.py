import rand_module
import data_retrieving_module


# TODO
# add text, audio, video etc. processing
def send_msg_to_user(vk, user_id, reply_dict):
    send_msg(vk, 'user_id', user_id, reply_dict)


def send_msg_to_chat(vk, chat_id, reply_dict):
    send_msg(vk, 'chat_id', chat_id, reply_dict)


def send_msg(vk, address_str, _id, reply_dict):
    vk.method(
        'messages.send',
        {
            address_str: _id, 'message': reply_dict.get('text'),
            'attachment': data_retrieving_module.retrieve_data(reply_dict),
            'random_id': rand_module.get_random_id()
        }
    )
