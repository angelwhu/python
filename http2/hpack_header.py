from hpack import Encoder, Decoder
e = Encoder()
d = Decoder()
with open('hpack.res', 'r') as f:
    print d.decode(f.read())
# [(u':status', u'200'), (u'server', u'nginx/1.14.0 (Ubuntu)'), (u'date', u'Wed, 30 Jan 2019 12:40:04 GMT'), (u'content-type', u'text/html; charset=UTF-8'), (u'set-cookie', u'F1ag:flag{Http2_Mak3_a_Differ3nce}=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0')]
