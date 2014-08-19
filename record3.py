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
        #if switch:#-1“≤ «True,µº÷¬”¿‘∂True
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

    #if 'mouse left down'==event.MessageName:
    #    print('mouse left down')
    #if 'mouse left up'==event.MessageName:
    #    print('mouse left up')
    
    if 'mouse move'==event.MessageName:
        global l1
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
hm.MouseMove = OnMouseEvent
# hook into the mouse and keyboard events
hm.HookKeyboard()

import pythoncom
pythoncom.PumpMessages()






