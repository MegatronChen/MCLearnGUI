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


# # Example7.17
# from tkinter import *
#
# def greeting():
#     print('Hello stdout world!...')
#
# win = Frame()
# win.pack()
# Label(win,text='Hello container world').pack(side=TOP)
# Button(win,text='Hello',command=greeting).pack(side=LEFT)
# Button(win,text='Quit',command=win.quit).pack(side=RIGHT)
#
# win.mainloop()


# 2018.05.15
# Lenovo received
# Mac learn
# Example7.18
# from tkinter import *
#
# class HelloButton(Button):
#     def __init__(self,parent=None,**config):
#         Button.__init__(self,parent,**config)
#         self.pack()
#         self.config(command=self.callback)
#
#     def callback(self):
#         print('Goodbye world...')
#         self.quit()
#
# # if __name__=='__main__':
# #     HelloButton(text='Hello subclass world').mainloop()
#
#
# # Example7.19
# class MyButton(HelloButton):
#     def callback(self):
#         print('Ignoring press!...')
#
# if __name__=='__main__':
#     MyButton(None,text='Hello subclass world').mainloop()



# Chapter8
# # Example8.1
# from tkinter import *
# root = Tk()
# lablefont = ('times',20,'bold')
# widget = Label(root,text='Hello config world')
# widget.config(bg='black',fg='yellow')
# widget.config(font=lablefont)
# widget.config(height=3,width=20)
# widget.pack(expand=YES,fill=BOTH)
# root.mainloop()


# # Example8.3
# import sys
# from tkinter import Toplevel,Button,Label
#
# win1 = Toplevel()
# win2 = Toplevel()
#
# Button(win1,text='Spam',command=sys.exit).pack()
# Button(win2,text='SPAM',command=sys.exit).pack()
#
# Label(text='Popups').pack()
# win1.mainloop()
# import sys
# help(sys.exit)


# # Example8.5
# from tkinter import *
# root = Tk()
#
# trees = [('The Larch!','light blue'),
#          ('The Pine!','light green'),
#          ('The Giant Redwood!','red')]
#
# for (tree,color) in trees:
#     win = Toplevel(root)
#     win.title('Sing...')
#     win.protocol('WM_DELETE_WINDOW',lambda:None)
#     win.iconbitmap('py-blue-trans-out.ico')
#
#     msg = Button(win,text=tree,command=win.destroy)
#     msg.pack(expand=YES,fill=BOTH)
#     msg.config(padx=10,pady=10,bd=10,relief=RAISED)
#     msg.config(bg='black',fg=color,font=('times',30,'bold italic'))
#
# root.title('Lumberjack demo')
# Label(root,text='Main window',width=30).pack()
# Button(root,text='QUIT ALL',command=root.quit).pack()
# root.mainloop()



# # Example8.6
# from tkinter import *
# from tkinter.messagebox import *
#
# def callback():
#     if askyesno('Verify','Do you really want to quit?'):
#         showwarning('Yes','Quit not yet implemented')
#     else:
#         showinfo('No','Quit has been cancelled')
#
# errmsg = 'Sorry, no Spam allowed!'
# Button(text='Quit',command=callback).pack(fill=X)
# Button(text='Spam',command=lambda:showerror('Spam',errmsg)).pack(fill=X)
# mainloop()



# # Example8.7
# from tkinter import *
# from tkinter.messagebox import askokcancel
#
# class Quitter(Frame):
#     def __init__(self,parent=None):
#         Frame.__init__(self,parent=None)
#         self.pack()
#         widget = Button(self,text='Quit',command=self.quit)
#         widget.pack(side=LEFT,expand=YES,fill=BOTH)
#
#     def quit(self):
#         ans = askokcancel('Verify exit','Really quit?')
#         if ans:
#             Frame.quit(self)
#
#
# # Example8.8
# from tkinter.filedialog import askopenfile
# from tkinter.colorchooser import askcolor
# from tkinter.messagebox import askquestion,showerror
# from tkinter.simpledialog import askfloat
#
# demos={
#     'Open': askopenfile,
#     'Color': askcolor,
#     'Query': lambda: askquestion('Warning','You typed "rm*"\nConfirm?'),
#     'Error': lambda: showerror('Error!',"He's dead, Jim"),
#     'Nput': lambda: askfloat('Entry','Entry credit card number')
# }
#
#
# # Example8.9
# from tkinter import *
#
# class Demo(Frame):
#     def __init__(self,parent=None,**options):
#         Frame.__init__(self,parent,**options)
#         self.pack()
#         Label(self,text='Basic demos').pack()
#         for (key,value) in demos.items():
#             Button(self,text=key,command=value).pack(side=TOP,fill=BOTH)
#         Quitter(self).pack(side=TOP,fill=BOTH)
#
# Demo().mainloop()


# import tkinter.filedialog
# help(tkinter.filedialog)
from tkinter.filedialog import *
# filelist = askopenfilenames()
# print(type(filelist))