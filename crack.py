import sys
import crypt, getpass, pwd
import string
import hashlib

def md5(src):
    m2 = hashlib.md5()
    m2.update(src)
    return m2.hexdigest()

def crack(deep,pw):
    if deep == 0:
        return;
    for c in string.printable[0:94]:
        crack(deep-1,pw + c)

        passwd  = pw + c
        crypted = md5(passwd)
        if crypted[0:6] == sys.argv[1]:
            print passwd
            print crypted
            print crypted[0:6]
            print "success"
            exit()
if __name__ == '__main__':
    crack(4,"")
