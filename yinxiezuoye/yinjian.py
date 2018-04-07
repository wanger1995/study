#!/usr/bin/env python
#coding:utf-8
from PIL import Image
import sys
if not(len(sys.argv)==2):
    print '用法：python  *.png'
try:
    im=Image.open(sys.argv[1])
except:
    print '图片打不开！'
pix=im.load()
sizex,sizey=im.size
for x in range(0,sizex):
    for y in range(0,sizey):
        if pix[x,y][0]%2==1:
            pix[x,y]=(0,0,0)
        else:
            pix[x,y]=(255,255,255)

im.show()
im.save(sys.argv[1]+'word.png','PNG')


