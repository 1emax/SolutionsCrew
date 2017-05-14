#coding: utf-8
import os
import requests
import json
import vkontakte
import time, datetime, calendar

# Час який додати до теперішнього часу в хв(вийде час відкладеного посту)
n = 0
# Зріз часу тобто інтервал  постінгу
y = 5

token = '88d2fe5dd5e008ea68c7674ce96e9b5c08c361d6ddaae3d69f2df0c2cdbc11135fa8b5f0ded09552ebcdc'
vkapi = vkontakte.API(token=token)
# Ідентифікатор групи
groupid = -109992198
# imagefolder = '/home/artem/Desktop/All/Projects/ShevaVK/images'
imagefolder = os.path.join('images')


def post_post(groupid, message, token, filepath, publish, n):
    try:
        # Шлях до зображення
        img = {'photo': ('img.jpg', open(filepath, 'rb'))}

        # Отримаємо посилання для завантаження фото
        method_url = 'https://api.vk.com/method/photos.getWallUploadServer?'
        data = dict(access_token=token, groupid=groupid)
        trigger3 = True
        while trigger3:
            try:
                response = requests.post(method_url, data, timeout=(10))
                trigger3 = False
            except Exception as e:
                trigger3 = False
                # time.sleep(3)
                print(e, 'too long trying onemore1')
        result = json.loads(response.text)
        upload_url = result['response']['upload_url']

        # Завантажуємо фото на посилання
        print('Завантажуємо фото на посилання')
        trigger2 = True
        while trigger2:
            try:
                response = requests.post(upload_url, files=img, timeout=(10))
                trigger2 = False
            except Exception as e:
                time.sleep(3)
                trigger2 = False
                print(e, 'too long passing')
        result = json.loads(response.text)


        # Зберігаємо фото на сервері і отримуємо id
        method_url = 'https://api.vk.com/method/photos.saveWallPhoto?'
        data = dict(access_token=token, groupid=groupid, photo=result['photo'], hash=result['hash'], server=result['server'])
        trigger6 = True
        while trigger6:
            try:
                response = requests.post(method_url, data)
                trigger6 = False
            except Exception as e:
                print('sleeeping 2s', e)
                trigger6 = False
                time.sleep(2)
        result = json.loads(response.text)['response'][0]['id'] + ',http://www.shevaforyou.info'

        # Видаляємо зображення
        os.remove(filepath)

        # Тепер цей id передаємо в attachments методу wall.post. Перевіряємо шоб точно пост був створений завдяки while
        print('Тепер цей id передаємо в attachments методу wall.post')
        trigger = True
        while trigger:
            try:
                vkapi.wall.post(owner_id=str(groupid), from_group=1, message=message, attachments=result)
                trigger = False
            except vkontakte.api.VKError as e2:
                if ('Access to adding post denied: a post is already scheduled for this time' in str(e2)) == True:
                    n = n + 10
                    print('Error: time colision, changing time to', n)
                    publish = calendar.timegm((now + datetime.timedelta(minutes=n)).timetuple())
                    time.sleep(0.5)
                    # quit()
                elif ('Access to adding post denied: can only schedule 25 posts on a day' in str(e2)) == True:
                    print('Sheduled posts Limit, quiting')
                    quit()
                elif ('Access to adding post denied: cannot postpone post' in str(e2)) == True:
                    print('Day Limit riched, quiting')
                    quit()
                else:
                    print(e2)
            except Exception as e3:
                print('error', e3)
                print('trying one more')
                trigger = False
        # if success вертаємо час останього посту
        return n
    except:
        n = 0
        return n


now = datetime.datetime.utcnow()
counter = 0
sheduledtime = calendar.timegm((now + datetime.timedelta(minutes=n)).timetuple())

message = "test"
print('here')
post_post(groupid, message, token, 'test.jpg', sheduledtime, n)
