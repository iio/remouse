# -*- coding: utf-8 -*-
import pickle,time

switch=-1
l1=[]
firstTime=True
previousTime = 0

def OnKeyboardEvent(event):
    if 'Space'==event.Key:
        #print 'Space'
        global switch
        switch=switch*-1
        #print switch
        if switch>0:
        #if switch:#-1也是True,导致永远True
            print('start')

            #初始化
            global l1
            l1=[]
            global firstTime
            firstTime=True
            global previousTime
            previousTime = 0

            hm.HookMouse()
        else:
            hm.UnhookMouse()
            print(l1)
            
            pickle.dump(l1,open('cc','w'))
            print('finished')

    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True


def OnMouseEvent(event):
    #print 'MessageName:',event.MessageName
    #print 'Message:',event.Message
    #print 'Time:',event.Time
    #print 'Window:',event.Window
    #print 'WindowName:',event.WindowName
    #print 'Position:',event.Position
    #print 'Wheel:',event.Wheel
    #print 'Injected:',event.Injected
    #print '---'
    #print dir(event)
    if event.MessageName in ['mouse left down','mouse left up','mouse move']:#只记录list中的Message,其他Message忽略

        global l1
        global previousTime
        global firstTime
        if firstTime:#记录 第一次
            print('im first')
            previousTime = time.clock()
            firstTime=False
        else:
            l1.append(time.clock()-previousTime)
            previousTime = time.clock()


        if 'mouse left down'==event.MessageName:
            #print('mouse left down')
            l1.append('d')
        if 'mouse left up'==event.MessageName:
            #print('mouse left up')
            l1.append('u')
        if 'mouse move'==event.MessageName:
            #print(event.Position)
            l1.append(event.Position)
        
        
    #return True to pass the event to other handlers
    #return False to stop the event from propagating
    return True

#--------------
import pyHook

# create the hook mananger
hm = pyHook.HookManager()
# register  callbacks
hm.KeyDown = OnKeyboardEvent

hm.MouseLeftUp = OnMouseEvent
hm.MouseLeftDown = OnMouseEvent#注释该行 就可以 不记录 该Event
hm.MouseMove = OnMouseEvent
# hook into the mouse and keyboard events
hm.HookKeyboard()

import pythoncom
pythoncom.PumpMessages()






