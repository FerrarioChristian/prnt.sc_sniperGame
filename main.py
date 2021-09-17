import webbrowser
import random
from pynput import keyboard

n = random.randint(100000, 999999)

linkStr = "www.prnt.sc\\"
controller = keyboard.Controller()


def on_press(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.space:
        controller.press(keyboard.Key.ctrl)
        controller.press('w')
        controller.release(keyboard.Key.ctrl)
        controller.release('w')
        n = random.randint(100000, 999999) 
        webbrowser.open(linkStr + str(n), new = 1)


listener = keyboard.Listener(on_press = on_press)
listener.start()
listener.join() 
