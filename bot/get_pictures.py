import random


def get(vk_session, id_group, vk, count):
    try:
        max_num = vk.photos.get(owner_id=id_group, album_id='wall', count=0)['count']

        num = random.randint(1, max_num)
        pictures = vk.photos.get(owner_id=str(id_group), album_id='wall', count=count, offset=num)['items']
        buf = []
        for element in pictures:
            buf.append('photo' + str(id_group) + '_' + str(element['id']))
        attachment = ','.join(buf)
        print(attachment)
        return attachment
    except:
        return get(vk_session, id_group, vk)
