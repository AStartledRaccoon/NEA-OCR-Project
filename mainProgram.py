#main program space
#Callum Cafferty
#NEA
import os
from os.path import expanduser
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
class GUI(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.__root=master
        self.__root.title("OCR AI")
        self.grid()
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        blankimg=Image.open("transparent.png")
        self.mainWindow(595,842,blankimg)
        self.__root.mainloop()
    def addImage(self):
        self.__filename=filedialog.askopenfilename(initialdir=expanduser('~/Pictures'),title="Select file",filetypes=(("png files","*.png"),("all files","*.*")))
        self.__userimg=Image.open(self.__filename)
        imgsize=self.__userimg.size
        while imgsize[0]>1600 or imgsize[1]>900:
            imgsize=[int(i//1.05) for i in imgsize]
            print (imgsize)
        self.__userimg=self.__userimg.resize(imgsize,resample=Image.LANCZOS)    
        self.mainWindow(*imgsize,self.__userimg)
    def mainWindow(self,x,y,img):
        self.__imgdisplay=ImageTk.PhotoImage(img)
        self.__canvas=Canvas(self.__root,width=x,height=y)
        self.__canvas.grid(row=0)
        self.__canvas.create_image(0,0,image=self.__imgdisplay,anchor="nw")
        self.__imageButton=Button(self.__root, text="Import Image", command=self.addImage)
        self.__imageButton.grid(row=1)
instance=GUI(Tk())
    