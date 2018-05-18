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


# Example8.26
from tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self,parent=None,**options):
        Frame.__init__(self,parent,**options)
        self.pack()
        self.tools()
        Label(self,text='Check demos').pack()
        self.vars = []
        for key in demos:
            var = IntVar()
            Checkbutton(self,text=key,variable=var,
                        command=demos[key]).pack(side=LEFT)
            self.vars.append(var)

    def report(self):
        for var in self.vars:
            print(var.get(),end=' ')
        print()

    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        Button(frm,text='State',command=self.report).pack(fill=X)
        Quitter(frm).pack(fill=X)

Demo().mainloop()