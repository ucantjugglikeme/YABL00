import new_msg_controller_module


def handle_chat_msg(vk, event, group_id):
    chat_id = event.chat_id
    msg = event.object.message['text']
    new_msg_controller_module.handle_msg(
        vk, 'chat_id', chat_id, msg, group_id,
        event, 2000000000 + chat_id
    )
