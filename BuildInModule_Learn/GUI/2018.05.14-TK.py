__author__ = 'lenovo'
# 核心编程中的GUI章节案例训练

print('\n')


# 5.3.1
# import tkinter
# top = tkinter.Tk()
# lable = tkinter.Label(top,text='Hello World!')
# lable.pack()
# tkinter.mainloop()


# 5.3.2
# import tkinter
# top = tkinter.Tk()
# quit = tkinter.Button(top,text='Hello World!',command=top.quit)
# quit.pack()
# tkinter.mainloop()


# 5.3.3
# import tkinter
# top = tkinter.Tk()
# quit = tkinter.Button(top,text='Hello World!',command=top.quit)
# quit.pack()
# tkinter.mainloop()

# # 5.3.3
# import tkinter
# top = tkinter.Tk()
# hello = tkinter.Label(top,text='Hello World!')
# hello.pack()
#
# quit = tkinter.Button(top,text='QUIT!',command=top.quit,
#                       bg='red',fg='white')
# quit.pack(fill=tkinter.X, expand=1)
#
# tkinter.mainloop()


# # 5.3.4
# import tkinter as tk
#
# def resize(ev=None):
#     label.config(font='Helvetica -%d bold' % \
#         scale.get())
#
# top = tk.Tk()
# # help(top.geometry)
# # 注意：中间是字母x，不是乘号！！！
# top.geometry('250x150')
#
# label = tk.Label(top,text='Hello World!',
#                  font='Helvetica -12 bold')
# help(label.pack)
# label.pack(fill=tk.Y,expand=1)
#
# scale = tk.Scale(top,from_=10,to=40,
#                  orient=tk.HORIZONTAL,command=resize)
# scale.set(12)
# scale.pack(fill=tk.X,expand=1)
#
# quit = tk.Button(top,text='QUIT',command=top.quit,
#                  activeforeground='white',
#                  activebackground='red')
# quit.pack()
#
# tk.mainloop()


# 5.3.5
from functools import partial as pto
from tkinter import Tk,Button,X
from tkinter.messagebox import showinfo,showwarning,showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU,
}

critCB = lambda: showerror('Error','Error Button Pressed!')
warnCB = lambda: showwarning('Warning','Warning Button Pressed!')
infoCB = lambda: showinfo('Info','Info Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top,text='QUIT',command=top.quit,bg='red',fg='white').pack()

MyButton = pto(Button,top)
CritButton = pto(MyButton,command=critCB,bg='white',fg='red')
WarnButton = pto(MyButton,command=warnCB,bg='goldenrod1')
ReguButton = pto(MyButton,command=infoCB,bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=True)' % (
        signType.title(),eachSign,
        '.upper()' if signType==CRIT else '.title()')
    eval(cmd)
#help(eval)
top.mainloop()


# # 5.3.6
# import os
# from time import sleep
# from tkinter import *
#
# class DirList(object):
#     def __init__(self,initdir=None):
#         self.top = Tk()
#         self.label = Label(self.top,text='Directory Lister V1.1')
#         self.label.pack()
#
#         self.cwd = StringVar(self.top)
#
#         self.dir1 = Label(self.top,fg='blue',font=('Helvetica',12,'bold'))
#         self.dir1.pack()
#
#         self.dirfm = Frame(self.top)
#
#         self.dirsb = Scrollbar(self.dirfm)
#         self.dirsb.pack(side=RIGHT,fill=Y)
#
#         self.dirs = Listbox(self.dirfm,height=15,width=50,yscrollcommand=self.dirsb.set)
#         self.dirs.bind('<Double-1>',self.setDirAndGo)
#         self.dirsb.config(command=self.dirs.yview)
#         self.dirs.pack(side=LEFT,fill=BOTH)
#         self.dirfm.pack()
#
#         self.dirn = Entry(self.top,width=50,textvariable=self.cwd)
#         self.dirn.bind('<Return>',self.doLS)
#         self.dirn.pack()
#
#         self.bfm = Frame(self.top)
#         self.clr = Button(self.bfm,text='Clear',command=self.clrDir,
#                           activeforeground='white',
#                           activebackground='blue')
#         self.ls = Button(self.bfm,text='List Directory',
#                          command=self.doLS,
#                          activeforeground='white',
#                          activebackground='green')
#         self.quit = Button(self.bfm,text='QUIT',command=self.top.quit,
#                            activeforeground='white',
#                            activebackground='red')
#
#         self.clr.pack(side=LEFT)
#         self.ls.pack(side=LEFT)
#         self.quit.pack(side=LEFT)
#         self.bfm.pack(side=LEFT)
#
#         if initdir:
#             self.cwd.set(os.curdir)
#             self.doLS()
#
#     def clrDir(self,ev=None):
#         self.cwd.set('')
#
#     def setDirAndGo(self,ev=None):
#         self.last = self.cwd.get()
#         self.dirs.config(selectbackground='red')
#         check = self.dirs.get(self.dirs.curselection())
#         if not check:
#             check = os.curdir
#         self.cwd.set(check)
#         self.doLS()
#
#     def doLS(self,ev=None):
#         error = ''
#         tdir = self.cwd.get()
#         if not tdir:
#             tdir = os.curdir
#         if not os.path.exists(tdir):
#             error = tdir + ':no such file'
#         elif not os.path.isdir(tdir):
#             error = tdir + 'not a directory'
#
#         if error:
#             self.cwd.set(error)
#             self.top.update()
#             sleep(2)
#             # if not (hasattr(self,'last') and self.last)
#             #     self.last = os.curdir
#             self.cwd.set(self.last)
#             self.dirs.config(selectbackground='LightSkyBlue')
#             self.top.update()
#             return
#
#         self.cwd.set('FETCHING DIRECTORY CONTENTS...')
#         self.top.update()
#         dirlist = os.listdir(tdir)
#         dirlist.sort()
#         os.chdir(tdir)
#
#         self.dir1.config(text=os.getcwd())
#         self.dirs.delete(0,END)
#         self.dirs.insert(END,os.curdir)
#         self.dirs.insert(END,os.pardir)
#         for eachFile in dirlist:
#             self.dirs.insert(END,eachFile)
#         self.cwd.set(os.curdir)
#         self.dirs.config(selectbackground='LightSkyBlue')
#
#
# def main():
#     d = DirList(os.curdir)
#     mainloop()
#
# if __name__ == '__main__':
#     main()

