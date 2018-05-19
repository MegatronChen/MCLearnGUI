__author__ = 'MC——lenovo'
'''
PPT-Counter Version0.1 powered by MC
count the total pages of all the ppt files(.pptx,.ppt) in a dictionary(and its subdir)
packed in GUI-just a simple root-TY() and a messagebox to show the result
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


root = Tk()
Label(root,text='查询中...').pack(expand=YES,fill=BOTH)

PPTFiles = []
def getPPTFiles(path):
    for subPath in os.listdir(path):
        subPath = os.path.join(path,subPath)
        if os.path.isdir(subPath):
            getPPTFiles(subPath)
        elif subPath.endswith(('.ppt','.pptx')):
            PPTFiles.append(subPath)
    return PPTFiles

def pptSlidesCount(path):
    PPT_App = win32com.client.Dispatch('Powerpoint.Application')
    CurrentPPT = PPT_App.Presentations.Open(path)
    CurrentPPTSlides = len(CurrentPPT.Slides)
    CurrentPPT.Close()
    PPT_App.Quit()
    return CurrentPPTSlides

def TransformName(CurrentPath,PPTFiles):
    RegularPPTs = []

    os.chdir(CurrentPath)
    if os.path.exists('_TemporaryDir'):
        shutil.rmtree('_TemporaryDir')
    os.mkdir('_TemporaryDir')
    TempDir = os.path.join(CurrentPath,'_TemporaryDir')
    os.chdir(TempDir)
    TargetDir = os.getcwd()

    for originPPT in PPTFiles:
        originpath,originfname = os.path.split(originPPT)
        shutil.copyfile(originPPT,os.path.join(TargetDir,originfname))

    os.chdir(TargetDir)
    DuplicatePPT_Names = os.listdir(TargetDir)

    for name in DuplicatePPT_Names:
        ChangeName = os.path.join(TargetDir,re.sub(r'\s+',r'-',name))
        os.rename(os.path.join(TargetDir,name),ChangeName)
        # RegularPPTs.append(os.path.join(TargetDir,re.sub(r'\s+',r'-',name))
        RegularPPTs.append(ChangeName)

    # return RegularPPTs

    return RegularPPTs



CurrentPath = askdirectory()
PPTFiles_Origin = getPPTFiles(CurrentPath)
PPTFiles = TransformName(CurrentPath,PPTFiles_Origin)
print(PPTFiles)

FilesCount = len(PPTFiles)
print('\n')
print('...Congratulations! Step1-Get all the ppt files succesfully!')
print(PPTFiles)

PPTPages = []
for EveryPPT in PPTFiles:
    print('\n')
    print(EveryPPT)
    PPTPage = pptSlidesCount(EveryPPT)
    PPTPages.append(PPTPage)


# for EveryPPT in PPTFiles:
#     # try:
#         PPTPage = pptSlidesCount(EveryPPT)
#     # except pywintypes.com_error:
#     #     pass
#     PPTPages.append(PPTPage)

PPTPages = list(PPTPages)

TotalPages = sum(PPTPages)
print('...Congratulations! Step2-Count total pages succesfully!')
print('*'*20+'当前目录下所有ppt文件共{FilesCountStr}个、{TotalPagesStr}页'.format(FilesCountStr=FilesCount,TotalPagesStr=TotalPages)+'*'*20)

ResultString = '当前目录下所有ppt文件共{FilesCountStr}个、{TotalPagesStr}页'.format(FilesCountStr=FilesCount,TotalPagesStr=TotalPages)
showinfo('Result',ResultString)



# BACKUP
# import tkinter.filedialog
# help(tkinter.filedialog)
