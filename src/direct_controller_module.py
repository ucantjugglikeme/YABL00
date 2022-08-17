import src.new_msg_controller_module as new_msg_controller_module


def handle_direct_msg(vk, event, group_id):
    user_id = event.object.message['from_id']
    peer_id = event.object.message['peer_id']
    msg = event.object.message['text']
    new_msg_controller_module.handle_msg(
        vk, 'user_id', user_id,
        msg, group_id, event, peer_id
    )
