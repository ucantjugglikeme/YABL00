import replying_module
import response_module


def handle_direct_msg(vk, event):
    user_id = event.object.message['from_id']
    msg = event.object.message['text']

    reply_dict = response_module.get_response_if_kw(msg)
    if reply_dict is not None:
        replying_module.send_msg_to_user(vk, user_id, reply_dict)
