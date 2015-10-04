'''
    Author : angelwhu
    Created time :  2015/10/03
    Description :  run.py
'''

import sys
import argparse
import GetPhoto

if __name__ == '__main__':
    #reload(sys)
    #sys.setdefaultencoding('gbk')
    parser = argparse.ArgumentParser(description='Process download photo.')
    parser.add_argument('-f', '--filename', help='filename to read')

    args = parser.parse_args()
    print args.filename

    photos = GetPhoto.GetPhotos(args.filename);
    photos.go();
