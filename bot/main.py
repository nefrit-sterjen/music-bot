from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
import get_pictures
import get_faggot
import create_post
import get_audio
import get_shit_pasta
import read_audio

token = "71422acb612bfd91f6f2b3b12b63024d8772614a4a112ac23644853241b3b72350506ec2c47510193e785"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
vk_session.api_version = 5.103

'''
def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'клава':

        keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Зеленая кнопка', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Красная кнопка', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)

    elif response == 'привет':
        keyboard.add_button('Клава', color=VkKeyboardColor.POSITIVE)

    elif response == 'мемы':
        keyboard.add_button('Мемы', color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        print("Закрытие клавиатуры...")
        return keyboard.get_empty_keyboard()

    keyboard.get_keyboard()
    return keyboard
    '''


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',
                      {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, 2147483648),
                       "attachment": attachment, 'keyboard': keyboard})


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print("Текст сообщения: " + str(event.text))
            print(event.user_id)
            response = event.text.lower()

            if event.from_user and not (event.from_me):
                if response.find('привет') != -1:
                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Дарова, хуйло! Как делишки?))')
                elif response.find('мемы') != -1:
                    attachment = get_pictures.get(vk_session, -95958948, session_api, 5)
                    send_message(vk_session, 'user_id', event.user_id, message='Ну держи мемы:', attachment=attachment)
                elif response.find("работать") != -1:
                    attachment = get_pictures.get(vk_session, -95958948, session_api, 1)
                    attachment += ',' + read_audio.read()
                    create_post.create(-95958948, '#Ботопост_генератор_музыки_рандомный_мем', session_api, attachment)
                elif response.find("паста") != -1:
                    pasta = get_shit_pasta.get(session_api, -92157416)
                    send_message(vk_session, 'user_id', event.user_id, message='На, почитай:', attachment=pasta)
                elif response.find("музыка") != -1:
                    attachment = read_audio.read()
                    send_message(vk_session, 'user_id', event.user_id, message='Держи', attachment=attachment)

                    # send_message(vk_session, 'user_id', event.user_id, message='держи музыку', attachment="audio579295663_456239020")

            '''
            elif response == 'закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть', keyboard=keyboard)
            '''

        elif event.from_chat and not (event.from_me):

            if response.find("мемы") != -1:
                attachment = get_pictures.get(vk_session, -95958948, session_api)
                send_message(vk_session, 'chat_id', event.chat_id, message="Держите, уебаны, тупые!",
                             attachment=attachment)
            elif response.find("пидор") != -1:
                gay = get_faggot.get(event.chat_id, session_api)
                mes = "Главный пидор конфы - " + gay
                send_message(vk_session, 'chat_id', event.chat_id, message=mes)
            elif response.find("гомик подзалупный") != -1:
                send_message(vk_session, 'chat_id', event.chat_id,
                             message="Так это Ярослав Осипов! Я его вчера видел в гей клубе!!!",
                             attachment="photo381824347_457260615")

        print("-" * 30)
