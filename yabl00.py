import vk_api
import random
import reply_module

token_file = open("../YABL00_DATABASE/yabl00_token")
bot_token = token_file.read()
vk_session = vk_api.VkApi(token=bot_token)

while True:
    messages = vk_session.method(
        'messages.getConversations',
        {'offset': 0, 'count': 20, 'filter': 'unanswered'}
    )

    if messages['count'] == 0:
        continue

    text = messages['items'][0]['last_message']['text']
    user_id = messages['items'][0]['last_message']['from_id']

    reply_msg = reply_module.get_response_if_kw(text)
    if reply_msg:
        vk_session.method(
            'messages.send',
            {'user_id': user_id, 'message': reply_msg, 'random_id': random.randint(1, 1000)}
        )
