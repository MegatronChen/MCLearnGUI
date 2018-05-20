__author__ = 'Megatron_chen'

'''
PPT-Counter Version0.2 powered by MC-2018.05.20
count the total pages of all the ppt files(.pptx,.ppt) in a dictionary(and its subdir)
packed in GUI with class, Button and Messagebox and Quitter
compiled to *.exe
'''

print('\n')


import os
import os.path
import shutil
import re
import win32com
import win32com.client
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import *
from quitter import Quitter


class PPTCounter(Frame):
    def __init__(self,parent=NONE,**options):
        self.OriPPTFiles = []
        self.PPTFiles = []
        self.PPTPages = []
        self.CurrentPath = NONE

        self.ChooseFlag =  StringVar()
        self.ChooseFlag.set('To Choose...')
        self.CacluFlag =  StringVar()
        self.CacluFlag.set('Come On!')


        Frame.__init__(self,parent,**options)
        self.pack()

        L0 = Label(self,text='PPT pages counter V0.2')
        L0.config(font=('Times',20,'bold'))
        L0.pack(side=TOP,expand=YES,fill=X)

        row1 = Frame(self).pack(side=TOP,expand=YES,fill=X)
        Label(row1).pack(side=TOP)
        Button(row1,width=20,text='Choose a directory',command=self.ChooseDir).pack(side=TOP)
        L1 = Label(row1,textvariable=self.ChooseFlag)
        L1.config(height=2)
        L1.pack(side=TOP,fill=X)

        row2 = Frame(self).pack(side=TOP,expand=YES,fill=X)
        Label(row2).pack(side=TOP)
        Button(row2,width=20,text='Count the Pages',command=self.PageCount).pack(side=TOP)
        L2 = Label(row2,textvariable=self.CacluFlag)
        L2.config(height=2)
        L2.pack(side=TOP,fill=X)


    # Inner functions
    def getPPTFiles(self,path):
        for subPath in os.listdir(path):
            subPath = os.path.join(path, subPath)
            if os.path.isdir(subPath):
                self.getPPTFiles(subPath)
            elif subPath.endswith(('.ppt', '.pptx')):
                self.OriPPTFiles.append(subPath)
        return self.OriPPTFiles


    def TransformName(self,CurrentPath, PPTFiles):

        RegularPPTs = []

        os.mkdir('_TemporaryDir')
        TargetDir = os.path.join(CurrentPath, '_TemporaryDir')

        for originPPT in PPTFiles:
            originpath, originfname = os.path.split(originPPT)
            # shutil.copyfile(originPPT, os.path.join(TargetDir, originfname))
            shutil.copy(originPPT, TargetDir)

        os.chdir(TargetDir)
        DuplicatePPT_Names = os.listdir(TargetDir)

        for name in DuplicatePPT_Names:
            ChangeName = os.path.join(TargetDir, re.sub(r'\s+', r'-', name))
            os.rename(os.path.join(TargetDir, name), ChangeName)
            RegularPPTs.append(ChangeName)

        return RegularPPTs


    def pptSlidesCount(self,path):
        PPT_App = win32com.client.Dispatch('Powerpoint.Application')
        CurrentPPT = PPT_App.Presentations.Open(path)
        CurrentPPTSlides = len(CurrentPPT.Slides)
        CurrentPPT.Close()
        PPT_App.Quit()
        return CurrentPPTSlides


    # Button functions
    def ChooseDir(self):
        CurrentPath = askdirectory()
        self.CurrentPath = CurrentPath
        os.chdir(CurrentPath)
        if os.path.exists('_TemporaryDir'):
            shutil.rmtree('_TemporaryDir')
        OriPPTFiles = self.getPPTFiles(CurrentPath)
        self.PPTFiles = self.TransformName(CurrentPath, OriPPTFiles)
        self.ChooseFlag.set('Choose Done!')
        return self.PPTFiles


    def PageCount(self):
        self.CacluFlag.set('Counting...')
        if len(self.PPTFiles) == 0:
            showwarning('Wrong Operation!','Choose files first!')
            return
        else:
            for EveryPPT in self.PPTFiles:
                self.CacluFlag.set('Counting...')
                PPTPage = self.pptSlidesCount(EveryPPT)
                self.PPTPages.append(PPTPage)
            self.TotalPages = sum(self.PPTPages)
            self.CacluFlag.set('Counting Done!')
            ResultString = '当前目录下所有ppt文件共{FilesCountStr}个、{TotalPagesStr}页'.format(FilesCountStr=len(self.PPTFiles),TotalPagesStr=self.TotalPages)
            showinfo('Result',ResultString)
            return self.TotalPages


class PPTCounterQuit(Quitter,PPTCounter):
    def __init__(self,parent=None):
        Quitter.__init__(self,parent)

    def quit(self):
        ans = askokcancel('Verify exit','Really quit?')
        if ans:
            ans2 = askokcancel('About the Temporary Files','Delete the temporary files?')
            if ans2:
                if CurrentCounter.CurrentPath == NONE:
                    pass
                else:
                    os.chdir(CurrentCounter.CurrentPath)
                    shutil.rmtree('_TemporaryDir')
            Frame.quit(self)


root = Tk()
CurrentCounter = PPTCounter(root)
PPTCounterQuit(root).pack(side=RIGHT)
root.mainloop()