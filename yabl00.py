import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import direct_controller_module
import chat_controller_module

token_file = open("../YABL00_DATABASE/yabl00_token")
bot_token = token_file.read()
token_file.close()
group_id_file = open("../YABL00_DATABASE/group_id")
group_id = group_id_file.read()
group_id_file.close()
vk_session = vk_api.VkApi(token=bot_token)

long_poll = VkBotLongPoll(vk_session, int(group_id))

for event in long_poll.listen():
    match event.type:
        case VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                chat_controller_module.handle_chat_msg(vk_session, event, group_id)
            else:
                direct_controller_module.handle_direct_msg(vk_session, event, group_id)
