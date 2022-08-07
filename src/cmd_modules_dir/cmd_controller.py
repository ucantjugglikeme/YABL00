import enum
import json
from src import response_module, interaction_module


class Command(enum.Enum):
    keywords = 0
    anecdote = 1
    dall_e = 2
    who_dies = 3
    bored = 4
    cats = 5


class CommandController:
    def __init__(self):
        self.state = Command.keywords
        self.response = None

    def prepare_response(self, vk, msg, group_id, address_str, _id, peer_id):
        for state in Command:
            match state:
                case Command.keywords:
                    self.response = response_module.get_response_if_kw(msg)
                case Command.anecdote:
                    self.response = response_module.get_response_if_anecdote(msg, group_id)
                case Command.dall_e:
                    pass
                case Command.who_dies:
                    self.response = response_module.get_response_if_who_dies(
                        vk, msg, address_str, _id, peer_id, group_id
                    )
                case Command.bored:
                    self.response = response_module.get_response_if_bored(msg, group_id)
                case Command.cats:
                    self.response = response_module.get_response_if_cats(vk, msg, group_id)
            self.state = state
            if self.response is not None:
                break

    def complete_cmd(self, vk, address_str, _id, peer_id, msg_id):
        if self.response is None:
            return

        query_json = json.dumps({
            "peer_id": peer_id, "conversation_message_ids": [msg_id],
            "is_reply": True
        })

        match self.state:
            case Command.keywords:
                interaction_module.send_msg(
                    vk, address_str, _id, self.response
                )
            case Command.anecdote:
                interaction_module.reply_to_msg(
                    vk, address_str, _id, self.response, query_json
                )
            case Command.dall_e:
                pass
            case Command.who_dies:
                interaction_module.reply_to_msg(
                    vk, address_str, _id, self.response, query_json
                )
            case Command.bored:
                interaction_module.reply_to_msg(
                    vk, address_str, _id, self.response, query_json
                )
            case Command.cats:
                interaction_module.reply_to_msg(
                    vk, address_str, _id, '', query_json, self.response
                )
