import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
import time
import cv2
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *

def label_func(x): return x.parent.name
learn_inf = load_learner("C:/Users/programmer/Desktop/FallGuys/DD.pkl")
print("loaded learner")

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

    image = grab_screen(region=(50, 100, 799, 449))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image,(224,224))
    # cv2.imshow("Fall", image)
    # cv2.waitKey(1)
    start_time = time.time()
    action = learn_inf.predict(image)[0]

    #print(action[0])

    #action = random.randint(0,3)
    
    if action == "Nothing":
        #print("Doing nothing....")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == "Left":
        print("Going left....")
        keyboard.press("a")
        keyboard.release("d")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == "Right":
        print("Going right....")
        keyboard.press("d")
        keyboard.release("a")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == "Jump":
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