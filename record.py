# -*- coding: utf-8 -*-
import win32api as w

import time

l1=[]
while w.GetCursorPos()>(20,20):
    time.sleep(0.01)#������ ̫�ߣ��ᵼ�� �ļ� ̫��
    l1.append(w.GetCursorPos())

print('finished')


import pickle
pickle.dump(l1,open('cc','w'))

