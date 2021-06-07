import time
import read_audio
import get_pictures
import create_post
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api

token = "71422acb612bfd91f6f2b3b12b63024d8772614a4a112ac23644853241b3b72350506ec2c47510193e785"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

while True:
    attachment = get_pictures.get(vk_session, -95958948, session_api, 1)
    attachment += ',' + read_audio.read()
    create_post.create(-95958948, '#Ботопост_генератор_музыки_рандомный_мем', session_api, attachment)
    time.sleep(3600)