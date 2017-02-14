还原RGB文件：  

#-*- coding:utf-8 -*- 
from PIL import Image 
import re 

x = 882 
y = 114 

im = Image.new(\"RGB\",(x,y)) 
file = open('flag.txt') 

for i in range(0,x): 
    for j in range(0,y): 
        line = file.readline() 
        rgb = line.split(\",\") 
        im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2]))) 
im.save(\"ok.png\")

制作RGB文件：

from PIL import Image 

im = Image.open('flag.png') 
pix = im.load() 
width = im.size[0] 
height = im.size[1] 
for x in range(width): 
    for y in range(height): 
    rgb = pix[x, y] 
    print rgb

