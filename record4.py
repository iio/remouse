# -*- coding: utf-8 -*-
import pickle

switch=-1
l1=[]

def OnKeyboardEvent(event):
    if 'Space'==event.Key:
        #print 'Space'
        global switch
        switch=switch*-1
        #print switch
        if switch>0:
        #if switch:#-1也是True,导致永远True
            print('start')
            global l1
            l1=[]
            hm.HookMouse()
        else:
            hm.UnhookMouse()
            #print(l1)
            
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
    global l1
    if 'mouse left down'==event.MessageName:
        #print('mouse left down')
        l1.append(1)
    if 'mouse left up'==event.MessageName:
        #print('mouse left up')
        l1.append(0)
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






