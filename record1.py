# -*- coding: utf-8 -*-
import win32api as w

import time

l1=[]
savedpos = w.GetCursorPos()
l1.append(savedpos)#��¼ ��ʼ��

while w.GetCursorPos()>(20,20):
    time.sleep(0.01)#������ ̫�ߣ��ᵼ�� �ļ� ̫��
    curpos = w.GetCursorPos()
    if savedpos != curpos:#ֻ��¼ ����ı�ĵ�
        savedpos = curpos
        l1.append(savedpos)
        
print(l1)
print('finished')


import pickle
pickle.dump(l1,open('cc','w'))

