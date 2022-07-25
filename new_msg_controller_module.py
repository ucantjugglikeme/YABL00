import replying_module
import response_module
import json


def handle_msg(vk, address_str, _id, msg, group_id, event, peer_id):
    reply_dict = response_module.get_response_if_kw(msg)
    cmd_reply = response_module.get_response_if_cmd(msg, group_id)
    if reply_dict is not None:
        replying_module.send_msg(vk, address_str, _id, reply_dict)
    elif cmd_reply is not None:
        msg_id = event.message.get('conversation_message_id')
        query_json = json.dumps({
                "peer_id": peer_id, "conversation_message_ids": [msg_id],
                "is_reply": True
            })
        print(query_json)
        replying_module.reply_to_msg(
            vk, address_str, _id, cmd_reply, query_json
        )