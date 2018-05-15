__author__ = 'lenovo'
print('\n')


# 《python编程》GUI章节学习


# Chapter7
# # Example7.1
# from tkinter import Label
# widget = Label(None,text='Hello GUI world!')
# widget.pack()
# widget.mainloop()


# # Example7.6
# from tkinter import *
# Label(text='hello GUI world!').pack(expand=YES,fill=BOTH)
# mainloop()


# # Example7.8
# from tkinter import *
# root = Tk()
# widget = Label(root)
# widget.config(text='hello GUI world!')
# widget.pack(side=TOP,expand=YES,fill=BOTH)
# root.title('gui1g.py')
# root.mainloop()


# # Example7.10
# import sys
# from tkinter import *
# widget = Button(None,text='Hello Widget World',command=sys.exit)
# widget.pack()
# widget.mainloop()


# # Example7.11
# from tkinter import *
# root = Tk()
# Button(root,text='press',command=root.quit).pack(side=LEFT,expand=YES)
# root.mainloop()


# Example7.17
from tkinter import *

def greeting():
    print('Hello stdout world!...')

win = Frame()
win.pack()
Label(win,text='Hello container world').pack(side=TOP)
Button(win,text='Hello',command=greeting).pack(side=LEFT)
Button(win,text='Quit',command=win.quit).pack(side=RIGHT)

win.mainloop()
