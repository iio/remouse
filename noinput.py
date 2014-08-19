# -*- coding: utf-8 -*-
import pyHook

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

    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    #return False#屏蔽鼠标。鼠标只能移动,3个按键 失效
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
    #if 'Space'==event.Key:
    #    print 'yes'

    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    #return False#屏蔽键盘。所有按键失效。只有 菜单键 能弹出 菜单。
    return True

# create the hook mananger
hm = pyHook.HookManager()
# register two callbacks
hm.MouseAllButtonsDown = OnMouseEvent
hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events
hm.HookMouse()
hm.HookKeyboard()

if __name__ == '__main__':
  import pythoncom
  pythoncom.PumpMessages()
