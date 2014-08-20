import pyHook,os

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
        os.system('cls' if os.name=='nt' else 'clear')
        print(event.Position)
    
    #return True to pass the event to other handlers
    #return False to stop the event from propagating
    return True

def OnKeyboardEvent(event):
    #print 'MessageName:',event.MessageName
    #print 'Message:',event.Message
    #print 'Time:',event.Time
    #print 'Window:',event.Window
    #print 'WindowName:',event.WindowName
    #print 'Ascii:', event.Ascii, chr(event.Ascii)
    #print 'Key:', event.Key
    #print 'KeyID:', event.KeyID
    #print 'ScanCode:', event.ScanCode
    #print 'Extended:', event.Extended
    #print 'Injected:', event.Injected
    #print 'Alt', event.Alt
    #print 'Transition', event.Transition
    #print '---'
    if 'Space'==event.Key:
        print 'yes'
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True

# create the hook mananger
hm = pyHook.HookManager()
# register two callbacks
hm.MouseMove = OnMouseEvent

#hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events
hm.HookMouse()
#hm.HookKeyboard()

if __name__ == '__main__':
  import pythoncom
  pythoncom.PumpMessages()

print('tesdsdsafsdt')
