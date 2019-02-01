# -*- coding: UTF-8 -*-
import socket

a = open("response.res", "r").read()
s = socket.socket()
host = '127.0.0.1'
port = 2333
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print '连接地址：', addr
    c.send(a)

# curl --http2-prior-knowledge 127.0.0.1:2333
# nc -lvvv 2333 > res.txt
#