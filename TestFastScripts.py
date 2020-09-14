import random
import time
import cv2

from utils.getkeys import key_check
import pydirectinput
import keyboard
from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *
from utils.grabscreen import grab_screen

learn_inf = load_learner("export.pkl")
def label_func(x): return x.parent.name
learn_inf.predict('g1-j5.png')
#E:/GateCrash/Nothing/

# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

# Hold down W no matter what!
keyboard.press('w')

# Randomly pick action then sleep.
# 0 do nothing release everything ( except W )
# 1 hold left
# 2 hold right
# 3 Press Jump
while True:

    # Get our image and process
    image = grab_screen(region=(50, 100, 799, 449))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image,(224,224))

    action = random.randint(0,3)

    if action == 0:
        print("Doing nothing....")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == 1:
        print("Going left....")
        keyboard.press("a")
        keyboard.release("d")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == 2:
        print("Going right....")
        keyboard.press("d")
        keyboard.release("a")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == 3:
        print("JUMP!")
        keyboard.press("space")
        keyboard.release("a")
        keyboard.release("d")
        time.sleep(sleepy)

    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break

keyboard.release('W')