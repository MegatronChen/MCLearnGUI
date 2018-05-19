print('\n')

import os
import os.path
import shutil
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
            # print(subPath)
            PPTFiles.append(subPath)
    # print('PPTFiles:',PPTFiles)
    return PPTFiles

def pptSlidesCount(path):
    PPT_App = win32com.client.Dispatch('Powerpoint.Application')
    CurrentPPT = PPT_App.Presentations.Open(r'%s' % path)
    CurrentPPTSlides = len(CurrentPPT.Slides)
    CurrentPPT.Close()
    PPT_App.Quit()
    return CurrentPPTSlides

CurrentPath = askdirectory()
PPTFiles = getPPTFiles(CurrentPath)

os.chdir(CurrentPath)
if os.path.exists('_TemporaryDir'):
    shutil.rmtree('_TemporaryDir')
    # os.rmdir('_TemporaryDir')
os.mkdir('_TemporaryDir')
TempDir = os.path.join(CurrentPath, '_TemporaryDir')
os.chdir(TempDir)
TargetDir = os.getcwd()

for originPPT in PPTFiles:
    originpath, originfname = os.path.split(originPPT)
    shutil.copyfile(originPPT, os.path.join(TargetDir, originfname))

os.chdir(TargetDir)
DuplicatePPTs = os.listdir(TargetDir)
print(DuplicatePPTs)