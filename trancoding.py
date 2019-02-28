# coding=utf-8
#!/usr/local/bin/python2.7
import os
f = open('./result.txt','r')
for i in f.readlines():
    ee = i.split('gsrecord')
    m = ee[1].split('"')
    l = '/gensee/platform/bin/ucflash2hlstool /data/record10'+m[0]+' 0 10 1 1'
    os.system(l)
f.close()
