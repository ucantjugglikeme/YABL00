import interaction_module
import response_module
from cmd_modules_dir.cmd_controller import CommandController
import json


def handle_msg(vk, address_str, _id, msg, group_id, event, peer_id):
    # reply_dict = response_module.get_response_if_kw(msg)
    # cmd_anecdote = response_module.get_response_if_anecdote(msg, group_id)
    # cmd_dall_e = response_module.get_response_if_anecdote(msg, group_id)
    # if reply_dict is not None:
    #    replying_module.send_msg(vk, address_str, _id, reply_dict)
    # elif cmd_anecdote is not None:
    #    msg_id = event.message.get('conversation_message_id')
    #    query_json = json.dumps({
    #            "peer_id": peer_id, "conversation_message_ids": [msg_id],
    #            "is_reply": True
    #        })
    #    replying_module.reply_to_msg(
    #        vk, address_str, _id, cmd_anecdote, query_json
    #    )

    cmd_controller = CommandController()
    cmd_controller.prepare_response(vk, msg, group_id, address_str, _id, peer_id)
    # print(msg, _id, peer_id)
    cmd_controller.complete_cmd(
        vk, address_str, _id, peer_id,
        event.message.get('conversation_message_id')
    )
