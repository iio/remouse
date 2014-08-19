# -*- coding: utf-8 -*-
import win32api as w
import time
import thread

switch=-1

def OnKeyboardEvent(event):
    if 'Space'==event.Key:
        #print 'Space'
        global switch
        switch=switch*-1
        #print switch
        if switch>0:
        #if switch:#-1也是True,导致永远True
            thread.start_new_thread(logic,())
        
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True

def logic():
    print('start')
    l1=[]
    savedpos = w.GetCursorPos()
    l1.append(savedpos)#记录 初始点
    global switch
    while switch>0:
        time.sleep(0.01)#采样率 太高，会导致 文件 太大
        curpos = w.GetCursorPos()
        if savedpos != curpos:#只记录 坐标改变的点
            savedpos = curpos
            l1.append(savedpos)
            
    #print(l1)
    import pickle
    pickle.dump(l1,open('cc','w'))
    print('finished')

#--------------
import pyHook

# create the hook mananger
hm = pyHook.HookManager()
# register  callbacks
hm.KeyDown = OnKeyboardEvent

# hook into the keyboard events
hm.HookKeyboard()

import pythoncom
pythoncom.PumpMessages()






