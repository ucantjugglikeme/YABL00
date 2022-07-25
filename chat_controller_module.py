import replying_module
import response_module


def handle_chat_msg(vk, event, group_id):
    chat_id = event.chat_id
    msg = event.object.message['text']
 
    reply_dict = response_module.get_response_if_kw(msg)
    if reply_dict is not None:
        replying_module.send_msg_to_chat(vk, chat_id, reply_dict)
    else:
        response_module.get_response_if_cmd(msg, group_id)
