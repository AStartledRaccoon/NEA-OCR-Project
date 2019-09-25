#main program space
#Callum Cafferty
#NEA

import os
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
        self.mainWindow(595,842,blankimg,True)
        self.__root.mainloop()
    def imageDialog(self):
        self.__filename=filedialog.askopenfilename(initialdir=os.path.expanduser('~/Pictures'),title="Select file",filetypes=(("PNG Images","*.png"),("JPEG Images","*.jpg"),("All files","*.*")))
        self.__userimg=Image.open(self.__filename)
        self.addImage(self.__userimg,False)
    def addImage(self,img,rotate):
        imgsize=img.size
        print ("initial ","x: ",imgsize[0]," y: ",imgsize[1])
        while imgsize[0]>1600 or imgsize[1]>900:
            imgsize=[int(i//1.05) for i in imgsize]
            img=img.resize(imgsize,Image.LANCZOS)    
        self.mainWindow(*img.size,img,False)
    def imageRotate(self, clockwise, img):
        print (img.size)
        if clockwise==True:
            self.addImage(img.rotate(270,expand=1),True)
        else:
            self.addImage(img.rotate(90,expand=1),True)
    def crop(self,x,y):
        pass
    def mainWindow(self,x,y,img,init):
        if init==False:
            self.__canvas.grid_forget()
            self.__canvas.delete("all")
        self.__imgdisplay=ImageTk.PhotoImage(img)
        self.__canvas=Canvas(self.__root,width=x,height=y,highlightthickness=1, highlightbackground="black")
        self.__canvas.grid(row=0,padx=20,pady=10,columnspan=20)
        self.__canvas.create_image(0,0,image=self.__imgdisplay,anchor="nw")
        self.__imageButton=Button(self.__root, text="Import Image", command=self.imageDialog,anchor="e")
        self.__imageButton.grid(column=0,row=1,pady=10,padx=2)
        self.__antiIco=ImageTk.PhotoImage(file="Icons/anticlockwise.ico")
        self.__antiRotate=Button(self.__root,image=self.__antiIco,command=lambda: self.imageRotate(False,img),anchor="e")
        self.__antiRotate.grid(column=17,row=1,padx=2,pady=10)
        self.__clockwiseIco=ImageTk.PhotoImage(file="Icons/clockwise.ico")
        self.__clockRotate=Button(self.__root, image=self.__clockwiseIco,command=lambda: self.imageRotate(True,img),anchor="e")
        self.__clockRotate.grid(column=18,row=1,padx=2,pady=10)
        self.__cropIco=ImageTk.PhotoImage(file="Icons/crop.ico")
        self.__cropButton=Button(self.__root, image=self.__cropIco,command=lambda: self.crop(x,y),anchor="e")
        self.__cropButton.grid(column=19,row=1,padx=2,pady=10)
        if init==True:
            self.__antiRotate.config(state=DISABLED)
            self.__clockRotate.config(state=DISABLED)
            self.__cropButton.config(state=DISABLED)
instance=GUI(Tk())
    