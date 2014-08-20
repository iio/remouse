# -*- coding: utf-8 -*-
import pickle,time

# 从 文件中 读取并恢复 对象
l1 = pickle.load(open("cc", "r"))
 
#print l1
import win32api, win32con
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
        else:
            quit()
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True


def logic():
    print('start')
    #回放是 逆过程
    for i in l1:
        if 'd'==i:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        elif 'u'==i:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        elif 'tuple'==type(i).__name__:    
            win32api.SetCursorPos(i)
        else:
            time.sleep(i)
    print('finished')


#--------------
import pyHook

# create the hook mananger
hm = pyHook.HookManager()
# register  callbacks
hm.KeyDown = OnKeyboardEvent
# hook into the mouse and keyboard events
hm.HookKeyboard()

import pythoncom
pythoncom.PumpMessages()




