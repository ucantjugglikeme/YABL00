from src.cmd_executors.cmd_controller import CommandController


def handle_msg(vk, address_str, _id, msg, group_id, event, peer_id):
    cmd_controller = CommandController()
    cmd_controller.prepare_response(vk, msg, group_id, address_str, _id, peer_id)
    cmd_controller.complete_cmd(
        vk, address_str, _id, peer_id,
        event.message.get('conversation_message_id')
    )
