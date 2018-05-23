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
# # # Example8.9
# # from tkinter import *
# #
# # class Demo(Frame):
# #     def __init__(self,parent=None,**options):
# #         Frame.__init__(self,parent,**options)
# #         self.pack()
# #         Label(self,text='Basic demos').pack()
# #         for (key,value) in demos.items():
# #             Button(self,text=key,command=value).pack(side=TOP,fill=BOTH)
# #         Quitter(self).pack(side=TOP,fill=BOTH)
# #
# # Demo().mainloop()
#
#
# # import tkinter.filedialog
# # help(tkinter.filedialog)
# # from tkinter.filedialog import *
# # filelist = askopenfilenames()
# # print(type(filelist))
# # print(list(filelist))
#
#
# # Example8.10
# from tkinter import *
#
# class Demo(Frame):
#     def __init__(self,parent=None,):
#         Frame.__init__(self,parent)
#         self.pack()
#         Label(self,text='Basic demos').pack()
#         for key in demos:
#             func = (lambda key= key: self.printit(key))
#             Button(self,text=key,command=func).pack(side=TOP,fill=BOTH)
#         Quitter(self).pack(side=TOP,fill=BOTH)
#
#     def printit(self,name):
#         print(name,'returns =>',demos[name]())
#
# Demo().mainloop()


# # Example8.13
# import sys
# from tkinter import *
# # help(sys)
# makemodal = (len(sys.argv)>1)
# def dialog():
#     win = Toplevel()
#     Label(win,text='Hard drive reformatted!').pack()
#     Button(win,text='OK',command=win.destroy).pack()
#     if makemodal:
#         win.focus_set()
#         win.grab_set()
#         win.wait_window()
#     print('dialog exit')
#
# root = Tk()
# Button(root,text='group',command=dialog).pack()
# root.mainloop()


# # Example8.15
# from tkinter import *
# # help(event)
#
# def showPosEvent(event):
#     print('Widget=%s X=%s Y=%s' %(event.widget,event.x,event.y))
#
# def showAllEvent(event):
#     print(event)
#     for attr in dir(event):
#         if not attr.startswith('__'):
#             print(attr,'=>',getattr(event,attr))
#
# def onKeyPress(event):
#     print('got key press:',event.char)
#
# def onArrowKey(event):
#     print('got up arrow key press')
#
# def onReturnKey(event):
#     print('got return key press')
#
# def onLeftClick(event):
#     print('got left mouse button clcik: ',end=' ')
#     showPosEvent(event)
#
# def onRightClick(event):
#     print('got right mouse button clcik: ',end=' ')
#     showPosEvent(event)
#
# def onMiddleClick(event):
#     print('got middle mouse button clcik: ',end=' ')
#     showPosEvent(event)
#     showAllEvent(event)
#
# def onLeftDrag(event):
#     print('got left mouse button drag:',end=' ')
#     showPosEvent(event)
#
# def onDoubleLeftClick(event):
#     print('got double left mouse click',end=' ')
#     showPosEvent(event)
#     tkroot.quit()
#
# tkroot = Tk()
# lablefont = ('courier',20,'bold')
# widget = Label(tkroot,text='Hello bind world')
# widget.config(bg='red',font=lablefont)
# widget.config(height=5,width=20)
# widget.pack(expand=YES,fill=BOTH)
#
# widget.bind('<Button-1>',onLeftClick)
# widget.bind('<Button-3>',onRightClick)
# widget.bind('<Button-2>',onMiddleClick)
# widget.bind('<Double-1>',onDoubleLeftClick)
# widget.bind('<B1-Motion>',onLeftDrag)
#
# widget.bind('<KeyPress>',onKeyPress)
# widget.bind('<p>',onArrowKey)
# widget.bind('<Return>',onReturnKey)
# widget.focus()
# tkroot.title('Click Me')
# tkroot.mainloop()


# # Example8.17
# from tkinter import *
# def fetch():
#     print('input => "%s" ' % ent.get())
#
# root = Tk()
# ent = Entry(root)
# ent.insert(0,'Type words here')
# ent.pack(side=TOP,fill=X)
# ent.focus()
# ent.bind('<Return>',(lambda event:fetch()))
#
# btn = Button(root,text='Fetch',command=fetch)
# btn.pack(side=LEFT)
#
# Quitter(root).pack(side=RIGHT)
# root.mainloop()


# Example8.18
# from tkinter import *
# import sys
# print(sys.path)
# from quitter import Quitter as Quitter

# fields = 'Name','Job','Pay'

# def fetch(entries):
#     for entry in entries:
#         print('Input => "%s"' % entry.get())
#
# def makeform(root,fields):
#     entries = []
#     for field in fields:
#         row = Frame(root)
#         lab = Label(row,width=5,text=field)
#         ent = Entry(row)
#         row.pack(side=TOP,fill=X)
#         lab.pack(side=LEFT)
#         ent.pack(side=RIGHT,expand=YES,fill=X)
#         entries.append(ent)
#     return entries

# root = Tk()
# ents = makeform(root,fields)
# root.bind('<Return>',(lambda event: fetch(ents)))
# Button(root,text='Fetch',command=(lambda:fetch(ents))).pack(side=LEFT)
# Quitter(root).pack(side=RIGHT)
# root.mainloop()


# # Example8.19
# from tkinter import *
# from quitter import Quitter as Quitter
#
# fields = 'Name','Job','Pay'
# def show(entries,popup):
#     fetch(entries)
#     popup.destroy()
#
# def ask():
#     popup = Toplevel()
#     ents = makeform(popup,fields)
#     Button(popup,text='OK',command=(lambda:show(ents,popup))).pack()
#     popup.grab_set()
#     popup.focus_set()
#     popup.wait_window()
#
# root = Tk()
# Button(root,text='Dialog',command=ask).pack()
# root.mainloop()


# # Example8.20
# from tkinter import *
# from quitter import Quitter as Quitter
#
# fields = 'Name','Job','Pay'
#
# def fetch(variables):
#     for variable in variables:
#         print('Input => "%s"' % variable.get())
#
#
# def makeform(root, fields):
#     form = Frame(root)
#     left = Frame(form)
#     right = Frame(form)
#     form.pack(fill=X)
#     left.pack(side=LEFT)
#     right.pack(side=RIGHT, expand=YES, fill=X)
#
#
#     variables = []
#     for field in fields:
#         lab = Label(left, width=5, text=field)
#         ent = Entry(right)
#         lab.pack(side=TOP)
#         ent.pack(side=TOP, fill=X)
#         var = StringVar()
#         ent.config(text=var)
#         var.set('enter here')
#         variables.append(var)
#     return variables
#
# root = Tk()
# vars = makeform(root,fields)
# Button(root,text='Fetch',command=(lambda:fetch(vars))).pack(side=LEFT)
# Quitter(root).pack(side=RIGHT)
# root.bind('<Return>',(lambda event:fetch(vars)))
# root.mainloop()


# # Example8.22
# from tkinter import *
# from dialogTable import demos
# from quitter import Quitter
#
# class Demo(Frame):
#     def __init__(self,parent=None,**options):
#         Frame.__init__(self,parent,**options)
#         self.pack()
#         self.tools()
#         Label(self,text='Check demos').pack()
#         self.vars = []
#         for key in demos:
#             var = IntVar()
#             Checkbutton(self,text=key,variable=var,
#                         command=demos[key]).pack(side=LEFT)
#             self.vars.append(var)
#
#     def report(self):
#         for var in self.vars:
#             print(var.get(),end=' ')
#         print()
#
#     def tools(self):
#         frm = Frame(self)
#         frm.pack(side=RIGHT)
#         Button(frm,text='State',command=self.report).pack(fill=X)
#         Quitter(frm).pack(fill=X)
#
# Demo().mainloop()


# Example8.25
# from tkinter import *
# from dialogTable import demos
# from quitter import Quitter
#
# class Demo(Frame):
#     def __init__(self,parent=None,**options):
#         Frame.__init__(self,parent,**options)
#         self.pack()
#         Label(self,text='Radio demos').pack(side=TOP)
#         self.var = StringVar()
#         for key in demos:
#             Radiobutton(self,text=key,command=self.onPress,
#                         variable=self.var,
#                         value=key).pack(anchor=NW)
#             self.var.set(key)
#         Button(self,text='State',command=self.report).pack(fill=X)
#         Quitter(self).pack(fill=X)
#
#     def onPress(self):
#         pick = self.var.get()
#         print('you pressed',pick)
#         print('result:',demos[pick]())
#
#     def report(self):
#         print(self.var.get())
#
# Demo().mainloop()



# # Example8.26
# from tkinter import *
#
# root = Tk()
# var = StringVar()
# for i in range(10):
#     rad = Radiobutton(root,text=str(i),variable=var,value=str(i%3))
#     rad.pack(side=LEFT)
# var.set(' ')
# root.mainloop()


# # Example8.30
# from tkinter import *
# from dialogTable import demos
# from quitter import Quitter
#
# class Demo(Frame):
#     def __init__(self, parent=None, **options):
#         Frame.__init__(self, parent, **options)
#         self.pack()
#         Label(self,text='Scale Demos').pack()
#         self.var = IntVar()
#         Scale(self,label='Pick demo number',
#               command=self.onMove,
#               variable=self.var,
#               from_=0,
#               to=len(demos)-1).pack()
#         Scale(self, label='Pick demo number',
#               command=self.onMove,
#               variable=self.var,
#               from_=0,
#               to=len(demos) - 1,
#               length=200,tickinterval=1,
#               showvalue=YES,orient='horizontal').pack()
#         Quitter(self).pack()
#         Button(self,text='Run demo',command=self.onRun).pack(side=LEFT)
#         Button(self,text='State',command=self.report).pack(side=RIGHT)
#
#     def onMove(self,value):
#         print('in onMove',value)
#
#     def onRun(self):
#         pos = self.var.get()
#         print('You picked',pos)
#         demo = list(demos.values())[pos]
#         print(demo())
#
#     def report(self):
#         print(self.var.get())
#
# print(list(demos.keys()))
# Demo().mainloop()


# # Example8.31
# from tkinter import *
# root = Tk()
# scl = Scale(root,from_=-100,to=100,tickinterval=50,resolution=10)
# scl.pack(expand=YES,fill=Y)
#
# def report():
#     print(scl.get())
#
# Button(root,text='state',command=report).pack(side=RIGHT)
#
# root.mainloop()


# # Example8.32
# from tkinter import *
# from quitter import Quitter
#
# demoModules = ['demoDlg','demoCheck','demoRadio','demoScale']
# parts = []
# # help(__import__)
#
# def addComponents(root):
#     for demo in demoModules:
#         module = __import__(demo)
#         part = module.Demo(root)
#         part.config(bd=2,relief=GROOVE)
#         part.pack(side=LEFT,expand=YES,fill=BOTH)
#         parts.append(part)
#
# def dumpState():
#     for part in parts:
#         print(part.__module__ + ':',end=' ')
#         if hasattr(part,'report'):
#             part.report()
#         else:
#             print('none')
#
# root = Tk()
# root.title('Frame')
# Label(root,text='Multiple Frame demo',bg='white').pack()
# Button(root,text='States',command=dumpState).pack(fill=X)
# Quitter(root).pack(fill=X)
# addComponents(root)
# root.mainloop()


# # Example8.36
# from tkinter import *
#
# class Checkbar(Frame):
#     def __init__(self,parent=None,picks=[],side=LEFT,anchor=W):
#         Frame.__init__(self,parent)
#         self.vars = []
#         for pick in picks:
#             var = IntVar()
#             chk = Checkbutton(self,text=pick,variable=var)
#             chk.pack(side=side,anchor=anchor,expand=YES)
#             self.vars.append(var)
#
#     def state(self):
#         return [var.get() for var in self.vars]
#
# class Radiobar(Frame):
#     def __init__(self,parent=None,picks=[],side=LEFT,anchor=W):
#         Frame.__init__(self,parent)
#         self.var = StringVar()
#         self.var.set(picks[0])
#         for pick in picks:
#             rad = Radiobutton(self,text=pick,value=pick,variable=self.var)
#             rad.pack(side=side,anchor=anchor,expand=YES)
#
#     def state(self):
#         return self.var.get()
#
# if __name__ == '__main__':
#     root = Tk()
#     lng = Checkbar(root,['Python','C#','Java','C++'])
#     gui = Radiobar(root,['win','x11','mac'],side=TOP,anchor=NW)
#     tg1 = Checkbar(root,['All'])
#
#     gui.pack(side=LEFT)
#     lng.pack(side=TOP,fill=X)
#     tg1.pack(side=LEFT)
#     lng.config(relief=GROOVE,bd=2)
#     gui.config(relief=RIDGE,bd=2)
#
#     def allstates():
#         print(gui.state(),lng.state(),tg1.state())
#
#     from quitter import Quitter
#
#     Quitter(root).pack(side=RIGHT)
#     Button(root,text='Peek',command=allstates).pack(side=RIGHT)
#     root.mainloop()


# # Example8.42
# import PIL
# # from PIL import ImageTk
# import os,sys
# from tkinter import *
#
# imgdir = 'images'
# imgfile = 'python.gif'
# if len(sys.argv) > 1:
#     imgfile = sys.argv[1]
#     imgpath = os.path.join(imgdir,imgfile)
#
# win = Tk()
# win.title(imgfile)
# imgobj = PhotoImage(file=imgpath)
# Label(win,image=imgobj).pack()
# print(imgobj.width(),imgobj.height())
# win.mainloop()


# # Example8.43
# import os,sys
# from tkinter import *
# from PIL.ImageTk import PhotoImage
#
# imgdir = 'images'
# imgfile = '1.jpg'
# if len(sys.argv) > 1:
#     imgfile = sys.argv[1]
# imgpath = os.path.join(imgdir,imgfile)
#
# win = Tk()
# win.title(imgfile)
# imgobj = PhotoImage(file=imgpath)
# Label(win,image=imgobj).pack()
# win.mainloop()
# print(imgobj.width(),imgobj.height())


# # Example8.44
# import os,sys
# from tkinter import *
# from PIL.ImageTk import PhotoImage
#
# imgdir = 'images'
# if len(sys.argv) > 1:
#     imgdir = sys.argv[1]
# imgfiles = os.listdir(imgdir)
#
# main = Tk()
# main.title('Viewer')
# quit = Button(main,text='Quit All',command=main.quit,font=('courier',25))
# quit.pack()
# savephotos = []
#
# for imgfile in imgfiles:
#     imgpath = os.path.join(imgdir,imgfile)
#     win = Toplevel()
#     win.title(imgfile)
#     try:
#         imgobj = PhotoImage(file=imgpath)
#         Label(win,image=imgobj).pack()
#         print(imgpath,imgobj.width(),imgobj.height())
#         print('\n')
#         savephotos.append(imgobj)
#     except:
#         errmsg = 'skipping %s\n %s' % (imgfile,sys.exc_info()[1])
#         Label(win,text=errmsg).pack()
#
# main.mainloop()


# # Example8.45
# import os,sys,math
# from tkinter import *
# from PIL import Image
# from PIL.ImageTk import PhotoImage
# import pprint
#
#
# def makeThumbs(imgdir,size=(100,100),subdir='thumbs'):
#     thumbdir = os.path.join(imgdir,subdir)
#     if not os.path.exists(thumbdir):
#         os.mkdir(thumbdir)
#
#     thumbs = []
#     for imgfile in os.listdir(imgdir):
#         thumbpath = os.path.join(thumbdir,imgfile)
#         if os.path.exists(thumbpath):
#             thumbobj = Image.open(thumbpath)
#             thumbs.append((imgfile,thumbobj))
#         else:
#             print('making',thumbpath)
#             imgpath = os.path.join(imgdir,imgfile)
#             try:
#                 imgobj = Image.open(imgpath)
#                 imgobj.thumbnail(size,Image.ANTIALIAS)
#                 imgobj.save(thumbpath)
#                 thumbs.append(imgfile,imgobj)
#             except:
#                 print('Skipping:',imgpath,'\n')
#
#     return thumbs
#
#
# class ViewOne(Toplevel):
#     def __init__(self,imgdir,imgfile):
#         Toplevel.__init__(self)
#         self.title(imgfile)
#         imgpath = os.path.join(imgdir,imgfile)
#
#         imgobj = PhotoImage(file=imgpath)
#         Label(self,image=imgobj).pack()
#         print(imgpath,imgobj.width(),imgobj.height())
#         self.savephoto = imgobj
#
#
# def viewer(imgdir,kind=Toplevel,clos=None):
#     win = kind()
#     win.title('Viewer: ' + imgdir)
#     quit = Button(win,text='Quit',command=win.quit,bg='beige')
#     quit.pack(fill=X,side=BOTTOM)
#
#     thumbs = makeThumbs(imgdir)
#     if not clos:
#         clos = int(math.ceil(math.sqrt(len(thumbs))))
#
#     savephotos = []
#     while thumbs:
#         thumbsrow,thumbs = thumbs[:clos],thumbs[clos:]
#         row = Frame(win)
#         row.pack(fill=BOTH)
#         for (imgfile,imgobj) in thumbsrow:
#             # size = max(imgobj.size)
#             # print(imgobj.size)
#             photo = PhotoImage(imgobj)
#             link = Button(row,image=photo)
#             handler = lambda savefile=imgfile:ViewOne(imgdir,savefile)
#             link.config(command=handler)
#             link.pack(side=LEFT,expand=YES)
#             savephotos.append(photo)
#     return win,savephotos
#
# if __name__ == '__main__':
#     imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'images'
#     main,save = viewer(imgdir,kind=Tk)
#     main.mainloop()



# # Chapter9-from 2018.05.23
# # Example9.1
# from tkinter import *
# from tkinter.messagebox import *
#
# def notdone():
#     showerror('Not implemented', 'Not yet available')
#
# def makemenu(win):
#     top = Menu(win)
#     win.config(menu=top)
#
#     file = Menu(top)
#     file.add_command(label='New...',command=notdone,underline=0)
#     file.add_command(label='Open...',command=notdone,underline=0)
#     file.add_command(label='Quit...',command=win.quit,underline=0)
#     top.add_cascade(label='File',menu=file,underline=0)
#
#     edit = Menu(top,tearoff=False)
#     edit.add_command(label='Cut',command=notdone,underline=0)
#     edit.add_command(label='Paste',command=notdone,underline=0)
#     edit.add_separator()
#     top.add_cascade(label='Edit',menu=edit,underline=0)
#
#     submenu = Menu(edit,tearoff=False)
#     submenu.add_command(label='Spam',command=win.quit,underline=0)
#     submenu.add_command(label='Eggs',command=notdone,underline=0)
#     edit.add_cascade(label='Stuff',menu=submenu,underline=0)
#
# if __name__ == '__main__':
#     root = Tk()
#     root.title('menu_win')
#     makemenu(root)
#     msg = Label(root,text='Window menu basics')
#     msg.pack(expand=YES,fill=BOTH)
#     msg.config(relief=SUNKEN,width=40,height=7,bg='beige')
#     root.mainloop()


# # Example9.2
# root = Tk()
# for i in range(3):
#     win = Toplevel(root)
#     makemenu(win)
#     Label(win,bg='black',height=5,width=25).pack(expand=YES,fill=BOTH)
# Button(root,text='Bye',command=root.quit).pack()
# root.mainloop()


# # Example9.3
# from tkinter import *
# from tkinter.messagebox import *
#
# def notdone():
#     showerror('Not implemented', 'Not yet available')
#
# def makemenu(parent):
#     menubar = Frame(parent)
#     menubar.pack(side=TOP,fill=X)
#
#     fbutton = Menubutton(menubar,text='File',underline=0)
#     fbutton.pack(side=LEFT)
#     file = Menu(fbutton)
#     file.add_command(label='New...', command=notdone, underline=0)
#     file.add_command(label='Open...',command=notdone,underline=0)
#     file.add_command(label='Quit...',command=parent.quit,underline=0)
#     fbutton.config(menu=file)
#
#     ebutton = Menubutton(menubar,text='Edit',underline=0)
#     ebutton.pack(side=LEFT)
#     edit = Menu(ebutton,tearoff=False)
#     edit.add_command(label='Cut', command=notdone, underline=0)
#     edit.add_command(label='Paste',command=notdone,underline=0)
#     edit.add_separator()
#     ebutton.config(menu=edit)
#
#     submenu = Menu(edit,tearoff=True)
#     submenu.add_command(label='Spam', command=parent.quit, underline=0)
#     submenu.add_command(label='Eggs',command=notdone,underline=0)
#     edit.add_cascade(label='Stuff',menu=submenu,underline=0)
#
#     return menubar

# if __name__ == '__main__':
#     root = Tk()
#     root.title('menu_frm')
#     makemenu(root)
#     msg = Label(root, text='Window menu basics')
#     msg.pack(expand=YES,fill=BOTH)
#     msg.config(relief=SUNKEN,width=40,height=7,bg='beige')
#     root.mainloop()


# # Example9.4
# root = Tk()
# for i in range(2):
#     mnu = makemenu(root)
#     mnu.config(bd=2,relief=RAISED)
#     Label(root,bg='black',height=5,width=25).pack(expand=YES,fill=BOTH)
# Button(root,text='Bye',command=root.quit).pack()
# root.mainloop()


# # Example9.5
# root = Tk()
# for i in range(3):
#     frm = Frame()
#     mnu = makemenu(frm)
#     mnu.config(bd=2,relief=RAISED)
#     frm.pack(expand=YES,fill=BOTH)
#     Label(frm,bg='black',height=5,width=25).pack(expand=YES,fill=BOTH)
# Button(root,text='Bye',command=root.quit).pack()
# root.mainloop()


# # Example9.6
# from tkinter import *
# root = Tk()
# mbutton = Menubutton(root,text='Food')
# picks = Menu(mbutton)
# mbutton.config(menu=picks)
# picks.add_command(label='spam',command=root.quit)
# picks.add_command(label='eggs',command=root.quit)
# picks.add_command(label='bacon',command=root.quit)
# mbutton.pack()
# mbutton.config(bg='white',bd=4,relief=RAISED)
# root.mainloop()


# # Example9.7
# from tkinter import *
# root = Tk()
# var1 = StringVar()
# var2 = StringVar()
# opt1 = OptionMenu(root,var1,'spam','eggs','toast')
# opt2 = OptionMenu(root,var2,'ham','bacon','sausage')
# opt1.pack(fill=X)
# opt2.pack(fill=X)
# var1.set('spam')
# var2.set('ham')
#
# def state():
#     print(var1.get(),var2.get())
#
# Button(root,command=state,text='state').pack()
# root.mainloop()


# # Example9.8
# from tkinter import *
# from tkinter.messagebox import *
# from PIL.ImageTk import PhotoImage
#
# class NewMenuDemo(Frame):
#     def __init__(self,parent=None):
#         Frame.__init__(self,parent)
#         self.pack(expand=YES,fill=BOTH)
#         self.createWidgets()
#         self.master.title('Toolbars and Menus')
#         self.master.iconname('tkpython')
#
#     def createWidgets(self):
#         self.makeMenuBar()
#         self.makeToolBar()
#         L = Label(self,text='Menu and Toolbar Demo')
#         L.config(relief=SUNKEN,width=40,height=10,bg='white')
#         L.pack()
#
#     def makeToolBar(self):
#         toolbar = Frame(self,cursor='hand2',relief=SUNKEN,bd=2)
#         toolbar.pack(side=BOTTOM,fill=X)
#         Button(toolbar,text='Quit',command=self.quit).pack(side=RIGHT)
#         Button(toolbar,text='Hello',command=self.greeting).pack(side=LEFT)
#
#     def makeMenuBar(self):
#         self.menubar = Menu(self.master)
#         self.master.config(menu=self.menubar)
#         self.fileMenu()
#         self.editMenu()
#         self.imageMenu()
#
#     def fileMenu(self):
#         pulldown = Menu(self.menubar)
#         pulldown.add_command(label='Open...',command=self.notdone)
#         pulldown.add_command(label='Quit...',command=self.quit)
#         self.menubar.add_cascade(label='File',underline=0,menu=pulldown)
#
#     def editMenu(self):
#         pulldown = Menu(self.menubar)
#         pulldown.add_command(label='Paste',command=self.notdone)
#         pulldown.add_command(label='Spam',command=self.greeting)
#         pulldown.add_separator()
#         pulldown.add_command(label='Delete',command=self.greeting)
#         pulldown.entryconfig(4,state=DISABLED)
#         self.menubar.add_cascade(label='Edit',underline=0,menu=pulldown)
#
#     def imageMenu(self):
#         photoFiles = ('./images/1.jpg','./images/2.jpg','./images/3.png')
#         pulldown = Menu(self.menubar)
#         self.photoObjs = []
#         for file in photoFiles:
#             img = PhotoImage(file=file)
#             pulldown.add_command(image=img,command=self.notdone)
#             self.photoObjs.append(img)
#         self.menubar.add_cascade(label='Image',underline=0,menu=pulldown)
#
#     def greeting(self):
#         showinfo('greeting','Greetings')
#
#     def notdone(self):
#         showerror('Not implemented','Not yet avaliable')
#
#     def quit(self):
#         if askyesno('Verify quit','Are you sure you want to quit?'):
#             Frame.quit(self)
#
# if __name__ == '__main__':
#     NewMenuDemo().mainloop()