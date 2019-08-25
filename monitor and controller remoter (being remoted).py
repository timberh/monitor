from pynput.mouse import Button, Controller
from pynput import mouse, keyboard
from pynput.keyboard import Key 
import threading

mouse = Controller()

listener = mouse.Listener(   #monitoring the mouse
    on_move=onmove,
    on_click=onclick,
    on_scroll=onscroll)
listener.start()

def setmouse (x,y):#controlling mouse
    mouse.position = (x,y)

#controlling the mouse

def clickleft ():
    mouse.press(Button.left)
    mouse.release(Button.left)

def clickright ():
    mouse.press(Button.right)
    mouse.release(Button.right)

def pressleft ():
    mouse.press(Button.left)

def pressright():
    mouse.press(Button.right)

def releaseleft():
    mouse.realease(Button.left)

def relaeseright():
    mouse.release(Button.right)

def scroll(times):
    mouse.scroll(0,times)

#react for monitor

def onmove():


def onclick():


def onscroll():


#mouse end

#keyboard start

def clickkey(keykey):
    mouse.press(Key.keykey)
    mouse.release(Key.keykey)

def presskey(keykey):
    mouse.press(Key.keykey)

def releasekey(keykey):
    mouse.release(Key.keykey)

def typekey(word):
    mouse.type(word)

#manykey

def keys2 (key1,key2):       #two keys
    with mouse.pressed(key2):
        mouse.press(key1)
        mouse.release(key1)

def key3 (key1,key2,key3):
    with mouse.pressed(key1):
        with mouse.pressed(key2):
            mouse.press(key3)
            mouse.release(key3)

#monitor keyboard

def onpress(key):

def onrelease(key):


#keyboard end
