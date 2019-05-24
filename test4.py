from RBTree import RBT
from BSTree import BrokenTreeError
from frame import MainFrame
from tkinter import *
import random
import time

N = 10
L = list(range(N))
random.shuffle(L)

root = Tk()
rbt = RBT()
frame = MainFrame(root, rbt, speed=10, d=30, size=(800, 600))
rbt.add_frame(frame)

for i in range(N):
    rbt.insert(i, str(i))
    try:
        rbt.verify()
    except BrokenTreeError as e:
        rbt.prefix_traverse(['color'])
        print('Error node:', e.node)
        raise
rbt.prefix_traverse(['color'])
time.sleep(3)

print('#######################################')

# L = [0, 4, 3, 6, 5, 9, 8, 2, 1, 7]
random.shuffle(L)
for i in L:
    rbt.remove(i)
    # time.sleep(2)
    # rbt.frame.speed = 1
    try:
        rbt.verify()
    except BrokenTreeError as e:
        rbt.prefix_traverse(['color'])
        print('Error node:', e.node)
        raise
rbt.prefix_traverse(['color'])


root.mainloop()