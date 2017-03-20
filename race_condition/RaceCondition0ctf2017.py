__author__ = 'angelwhu'
# -*- coding:utf-8 -*-

import requests

import threading
from random import Random
import string

url = "http://202.120.7.197/app.php?action=login"

def random_str(randomlength=8):
    str = ''
    chars = string.ascii_lowercase + string.digits
    #print chars
    length = len(chars)
    #print length
    random = Random()
    for i in range(randomlength):
        temp = random.randint(0, length-1)
        #print temp
        str+=chars[temp]
    return str


def login_getmoney(cookies):
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Cookie": "PHPSESSID="+cookies,
               "Connection": "keep-alive"}
    datas = {"username": "angelwhutest123","pwd":"angelwhutest123"}
    r = requests.post(url, headers=headers, data=datas)
    print r.content

def buy(cookies):
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Cookie": "PHPSESSID="+cookies,
               "Connection": "keep-alive"}
    r = requests.post("http://202.120.7.197/app.php?action=buy&id=2", headers=headers)
    print r.content

def sale(cookies):
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Cookie": "PHPSESSID="+cookies,
               "Connection": "keep-alive"}
    r = requests.get("http://202.120.7.197/app.php?action=sale&id=2", headers=headers)
    print r.content

cookies_1 = "8o3lto4qdn4e0aasa2aog7gbg3"
cookies_2 = "le5af9o1qspgop8bp49v80sqs5"
cookies_3 = "vq828j22a80ahnclbfg33duuc2"
for i in range(0,300):
    #cookies = random_str(26)
    #print cookies
    threading.Thread(target=buy,args = (cookies_1,)).start()
    threading.Thread(target=sale,args = (cookies_2,)).start()
    threading.Thread(target=buy,args = (cookies_1,)).start()
    threading.Thread(target=sale,args = (cookies_3,)).start()
    threading.Thread(target=buy,args = (cookies_2,)).start()
    threading.Thread(target=sale,args = (cookies_1,)).start()
