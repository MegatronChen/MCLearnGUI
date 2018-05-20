__author__ = 'Megatron_chen'

'''
PPT-Counter Version0.2 powered by MC-2018.05.20
count the total pages of all the ppt files(.pptx,.ppt) in a dictionary(and its subdir)
packed in GUI with class, Button and Messagebox
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


class PPTCounter(Frame):
    def __init__(self,parent=None,**options):
        self.OriPPTFiles = []
        self.PPTFiles = []
        self.PPTPages = []

        self.ChooseFlag =  StringVar()
        self.ChooseFlag.set('To Choose...')
        self.CacluFlag =  StringVar()
        self.CacluFlag.set('Choose files first')


        Frame.__init__(self,parent,**options)
        self.pack()

        Label(self,text='PPT pages counter V0.2').pack(expand=YES,fill=X)

        row1 = Frame(self)
        Button(row1,text='Choose a directory',command=self.ChooseDir).pack(side=LEFT,fill=X)
        Label(row1,textvariable=self.ChooseFlag).pack(side=RIGHT,expand=YES,fill=X)

        row2 = Frame(self)
        Button(row2,text='Count the Pages',command=self.).pack(side=LEFT,fill=X)
        Label(row2,textvariable=self.CalcuFlag).pack(side=RIGHT,expand=YES,fill=X)


    # Inner functions
    def getPPTFiles(self,path):
        for subPath in os.listdir(path):
            subPath = os.path.join(path, subPath)
            if os.path.isdir(subPath):
                getPPTFiles(subPath)
            elif subPath.endswith(('.ppt', '.pptx')):
                self.OriPPTFiles.append(subPath)
        return self.OriPPTFiles


    def TransformName(CurrentPath, PPTFiles):

        RegularPPTs = []

        os.chdir(CurrentPath)
        if os.path.exists('_TemporaryDir'):
            shutil.rmtree('_TemporaryDir')
        os.mkdir('_TemporaryDir')
        TargetDir = os.path.join(CurrentPath, '_TemporaryDir')

        for originPPT in PPTFiles:
            originpath, originfname = os.path.split(originPPT)
            shutil.copyfile(originPPT, os.path.join(TargetDir, originfname))

        os.chdir(TargetDir)
        DuplicatePPT_Names = os.listdir(TargetDir)

        for name in DuplicatePPT_Names:
            ChangeName = os.path.join(TargetDir, re.sub(r'\s+', r'-', name))
            os.rename(os.path.join(TargetDir, name), ChangeName)
            RegularPPTs.append(ChangeName)

        return RegularPPTs


    def pptSlidesCount(path):
        PPT_App = win32com.client.Dispatch('Powerpoint.Application')
        CurrentPPT = PPT_App.Presentations.Open(path)
        CurrentPPTSlides = len(CurrentPPT.Slides)
        CurrentPPT.Close()
        PPT_App.Quit()
        return CurrentPPTSlides


    # Button functions
    def ChooseDir(self):
        CurrentPath = askdirectory()
        PPTFiles_Origin = self.getPPTFiles(CurrentPath)
        self.PPTFiles = self.TransformName(CurrentPath, PPTFiles_Origin)
        self.ChooseFlag.set('Choose Done!')
        return self.PPTFiles


    def PageCount(self):
        if len(self.PPTFiles) == 0:
            showwarning('Wrong','Choose files first!')
            return
        else:
            self.CacluFlag.set('Counting...')
            for EveryPPT in self.PPTFiles
                PPTPage = self.pptSlidesCount(EveryPPT)
                self.PPTPages.append(PPTPage)
            self.TotalPages = sum(PPTPages)
            ResultString = '当前目录下所有ppt文件共{FilesCountStr}个、{TotalPagesStr}页'.format(FilesCountStr=FilesCount,TotalPagesStr=TotalPages)
            showinfo('Result',ResultString)
            return self.TotalPages



