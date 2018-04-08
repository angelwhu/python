'''
    Author : angelwhu
    Created time :  2015/10/03
    Description :  write a download photo program
'''

import requests
from requests.auth import HTTPBasicAuth
import sys
from bs4 import BeautifulSoup

class GetPhotos(object):

    def __init__(self , filename):
        self.username = "******";
        self.password = "*****";
        self.vulnerability_url = "http://*****/attachmentDownload.portal?notUseCache=true&type=userPhoto&ownerId=";
        self.filename = filename;
        # "ziliao/cs-2015-graduate.csv"

        self.initXh();
        self.initSession();

    def initXh(self):
        self.xhMapList = [];
        for line in open(self.filename):
            li = line.strip().split(",");
            dict1 = {}
            dict1['kh'] = li[0];
            dict1['xm'] = li[1];
            dict1['xh'] = li[2];
            self.xhMapList.append(dict1);
            del dict1;
            #print self.xhMapList;

    def initSession(self):
        self.session = requests.Session()
        url = "https://*********/";
        post_data = {'IDToken1':self.username, 'IDToken2':self.password,
                     'IDButton':'Submit','goto':'aHR0cDovL215LndodS5lZHUuY24%3D','encoded':'true','gx_charset':'UTF-8'}

        headers = { "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.5",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Connection": "keep-alive"}
        response = self.session.post(url, headers=headers,data=post_data)
        #print u' '.join(response.text).encode('utf-8').strip();       # solve unicode error


    def downloadImageFile(self,imgUrl,imgName):
        print "Download Image File=", imgName
        r = self.session.get(imgUrl, stream=True) # here we need to set stream = True parameter
        with open("photos/" + imgName + ".jpg", 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
            f.close()

    def go(self):
        for dic in self.xhMapList :
            self.downloadImageFile(self.vulnerability_url + dic['xh'] , dic['xh'] + '-' + dic['xm']);

'''
    def test(self):
#        dic = self.xhMapList[0];
#        self.downloadImageFile(self.vulnerability_url + dic['xh'] , dic['xh'] + '-' + dic['xm']);
        dic1 = {'1':'ad','2':'fa'}
        dic2 = {'3':'xasdf','4':'fdafa'}

        list = []
        list.append(dic1)
        list.append(dic2)
        print list
'''
