# -*- coding: utf-8 -*-
import win32api as w

import time

l1=[]
savedpos = w.GetCursorPos()
l1.append(savedpos)#记录 初始点

while w.GetCursorPos()>(20,20):
    time.sleep(0.01)#采样率 太高，会导致 文件 太大
    curpos = w.GetCursorPos()
    if savedpos != curpos:#只记录 坐标改变的点
        savedpos = curpos
        l1.append(savedpos)
        
print(l1)
print('finished')


import pickle
pickle.dump(l1,open('cc','w'))

