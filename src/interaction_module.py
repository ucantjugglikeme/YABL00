import src.rand_module as rand_module
import src.data_retrieving_module as data_retrieving_module


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


def reply_to_msg(vk, address_str, _id, reply_msg, query_json, attachment=''):
    vk.method(
        'messages.send',
        {
            address_str: _id, 'message': reply_msg,
            'forward': query_json,
            'random_id': rand_module.get_random_id(),
            'attachment': attachment
        }
    )


def get_chat_info(vk, peer_id, group_id):
    return vk.method(
        'messages.getConversationMembers',
        {
            'peer_id': peer_id, 'group_id': group_id
        }
    )


def get_photo_msgs_upload_server(vk):
    return vk.method('photos.getMessagesUploadServer')


def get_saved_msgs_photo(vk, photo, server, hash_str):
    return vk.method(
        'photos.saveMessagesPhoto',
        {
            'photo': photo, 'server': server, 'hash': hash_str
        }
    )
