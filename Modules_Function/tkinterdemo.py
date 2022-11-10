try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

#
mainWindows = tkinter.Tk()

mainWindows.title("Hello World")
mainWindows.geometry("640x480+8+200")  # + - 是来改变位置的，朝右朝下移动为+，朝左朝上移动为-。

lable = tkinter.Label(mainWindows, text="Hello World")
lable.pack(side='top')

leftFrame = tkinter.Frame(mainWindows)
leftFrame.pack(side='left', achor='n', fill=tkinter.Y, expand=False)

# canvas = tkinter.Canvas(mainWindows, relief='raised', borderwidth=1)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindows)
rightFrame.pack(side='right', anchor='n', expand=True)
# 朝着某个方向延展的时候，如果没有延展成功就加上expand=True
# canvas.pack(side='left', fill=tkinter.Y)
# canvas.pack(side='left', fill=tkinter.X, expand=True)
# canvas.pack(side='top', fill=tkinter.X)
# canvas.pack(side='top', fill=tkinter.Y, expand=True)
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)

# button1 = tkinter.Button(mainWindows, text="button1")
# button2 = tkinter.Button(mainWindows, text="button2")
# button3 = tkinter.Button(mainWindows, text="button3")

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
# 当side是水平的左右时，anchor改变垂直的位置；当side是垂直的top/bottom时，anchor改变水平的位置。
# button1.pack(side='left', anchor='n')
# button2.pack(side='left', anchor='s')
# button3.pack(side='left', anchor='e')
# button1.pack(side='top', anchor='n')
# button2.pack(side='top', anchor='s')
# button3.pack(side='top', anchor='e')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')


mainWindows.mainloop()
#

