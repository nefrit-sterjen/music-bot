import random


def get(vk, id):
    try:
        offset = random.randint(1, 300)
        post = vk.wall.search(owner_id=id, query='#издач_говно', owners_only=1, count=100, offset=offset)['items']
        pasta = post[random.randrange(100)]
        link = 'wall' + str(id) + '_' + str(pasta['id'])
        return link
    except:
        return get(vk, id)
