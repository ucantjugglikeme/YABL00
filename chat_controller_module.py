import replying_module
import response_module


def handle_chat_msg(vk, event):
    chat_id = event.chat_id
    msg = event.object.message['text']

    reply_msg = response_module.get_response_if_kw(msg)
    if reply_msg is not None:
        replying_module.send_msg_to_chat(vk, chat_id, reply_msg)
