import time
import threading
from pynput.keyboard import Listener, KeyCode, Controller, Key

print("Auto Key Presser")
print("\nBy:  ViridianTelamon.")
time.sleep(2)
start_stop_key_input = input("\nEnter A Start And Stop Key (Make Sure The Letter Is Lowercase):  ")
time.sleep(0.2)
exit_key_input = input("\nEnter An Exit Key (Make Sure The Letter Is Lowercase):  ")
time.sleep(0.2)
delay_input = float(input("\nEnter A Number For The Delay Between The Certain Key Button Presses (It Can Be A Decimal If You Want As Well):  "))
time.sleep(0.2)
key_input = input("\nEnter The Key That You Want To Be Pressed Make Sure It Is Either Uppercase Or Lowercase (If You Want A Key That Is Space, Backspace, Shift, Control, Tab, Escape, Or Enter You Can Just Put Those In For It):  ")
time.sleep(0.2)
print("\nSetup Is Complete!  Press The Start Or Stop Or Exit Button That You Chose To The Auto Key Presser!")

if key_input == "space":
    key_input = Key.space
if key_input == "backspace":
    key_input = Key.backspace
if key_input == "shift":
    key_input = Key.shift
if key_input == "control":
    key_input = Key.ctrl
if key_input == "tab":
    key_input = Key.tab
if key_input == "escape":
    key_input = Key.esc
if key_input == "enter":
    key_input = Key.enter
else:
    key_input = key_input

delay = delay_input
button = key_input
start_stop_key = KeyCode(char=start_stop_key_input)
exit_key = KeyCode(char=exit_key_input)

class PressKey(threading.Thread):
    def __init__(self, delay, button):
        super(PressKey, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_pressing(self):
        self.running = True

    def stop_pressing(self):
        self.running = False

    def exit(self):
        self.stop_pressing()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                key_preser.press(self.button)
                key_preser.release(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


key_preser = Controller()
key_thread = PressKey(delay, button)
key_thread.start()


def on_press(key):
    if key == start_stop_key:
        if key_thread.running:
            key_thread.stop_pressing()
        else:
            key_thread.start_pressing()
    elif key == exit_key:
        key_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()