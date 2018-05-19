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
import win32com
import win32com.client
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import *


root = Tk()
Label(root,text='查询中...').pack(expand=YES,fill=BOTH)

def getPPTFiles(path):
    for subPath in os.listdir(path):
        subPath = os.path.join(path,subPath)
        if os.path.isdir(subPath):
            getPPTFiles(subPath)
        elif subPath.endswith(('.ppt','.pptx')):
            print(subPath)
            PPTFiles.append(subPath)

def pptSlidesCount(path):
    PPT_App = win32com.client.Dispatch('Powerpoint.Application')
    CurrentPPT = PPT_App.Presentations.Open(path)
    CurrentPPTSlides = len(CurrentPPT.Slides)
    CurrentPPT.Close()
    PPT_App.Quit()
    return CurrentPPTSlides

PPTFiles = []

CurrentPath = askdirectory()
getPPTFiles(CurrentPath)
FilesCount = len(PPTFiles)
print('\n')
print('...Congratulations! Step1-Get all the ppt files succesfully!')

PPTPages = []
for EveryPPT in PPTFiles:
    PPTPage = pptSlidesCount(EveryPPT)
    PPTPages.append(PPTPage)

PPTPages = list(PPTPages)

TotalPages = sum(PPTPages)
print('...Congratulations! Step2-Count total pages succesfully!')
print('*'*20+'当前目录下所有ppt文件共{FilesCountStr}个、{TotalPagesStr}页'.format(FilesCountStr=FilesCount,TotalPagesStr=TotalPages)+'*'*20)

ResultString = '当前目录下所有ppt文件共{FilesCountStr}个、{TotalPagesStr}页'.format(FilesCountStr=FilesCount,TotalPagesStr=TotalPages)
showinfo('Result',ResultString)



# BACKUP
# import tkinter.filedialog
# help(tkinter.filedialog)