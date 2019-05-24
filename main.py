from tkinter import *
from RBTree import RBT
from frame import MainFrame

def set_window(root):
    root.title('Red-Black-tree Visualization')
    root.resizable(True, True)


if __name__ == '__main__':
    root = Tk()
    set_window(root)

    rbt = RBT()
    frame = MainFrame(root, rbt, d=25, size=(800, 600))
    rbt.add_frame(frame)

    root.mainloop()
