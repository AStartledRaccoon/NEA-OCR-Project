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
        self.addImage(self.__userimg)
    def addImage(self,img):
        imgsize=img.size
        while imgsize[0]>1600 or imgsize[1]>900:
            imgsize=[int(i//1.05) for i in imgsize]
            img=img.resize(imgsize,Image.LANCZOS)    
        self.mainWindow(*img.size,img,False)
    def imageRotate(self, clockwise, img):
        if clockwise==True:
            self.addImage(img.rotate(270,expand=1))
        else:
            self.addImage(img.rotate(90,expand=1))
    def trainNetwork(self):
            pass
    def cancelCrop(self):
        self.__cropConfirm.destroy()
        self.__canvas.delete(self.__drawn)
        self.__cropButton.config(state="normal")
    def doCrop(self, event,img):
        self.__canvas.delete(self.__drawn)
        self.__cropConfirm.destroy()
        self.__cropImg=img.crop((self.__start.x, self.__start.y, event.x, event.y))
        self.__cropButton.config(state="normal")
        self.addImage(self.__cropImg)
    def cropEnd(self, event,img):
        self.__cropConfirm=Toplevel(self.__root)
        self.__cropConfirm.title("Crop")
        self.__canvas.config(cursor="")
        self.__canvas.unbind("<ButtonPress-1>")
        self.__canvas.unbind("<B1-Motion>")
        self.__canvas.unbind("<ButtonRelease-1>")
        self.__cropButtonA=Button(self.__cropConfirm,text="Confirm",command=lambda: self.doCrop(event,img))
        self.__cancelButton=Button(self.__cropConfirm,text="Cancel",command=self.cancelCrop)
        self.__cropLabel=Label(self.__cropConfirm, text="Crop selection?").grid(row=0, column=0, columnspan=2, padx=3, pady=3)
        self.__cropButtonA.grid(row=1, column=0, padx=3, pady=3)
        self.__cancelButton.grid(row=1, column=1, padx=3, pady=3)
        self.__cropConfirm.grid()
    def growRectangle(self,event):
        self.__canvas = event.widget
        if self.__drawn: self.__canvas.delete(self.__drawn)
        objectId = self.__shape(self.__start.x, self.__start.y, event.x, event.y,fill="gray50", stipple="gray50")
        self.__drawn = objectId     
    def startRectangle(self,event):
        self.__start=event
        self.__drawn=None
    def stopCrop(self,event):
        self.__canvas.unbind("<ButtonPress-1>")
        self.__canvas.unbind("<B1-Motion>")
        self.__canvas.unbind("<ButtonRelease-1>")
        self.__cropButton.config(state="normal")
    def crop(self,x,y,img):
        self.__cropButton.config(state=DISABLED)
        self.__canvas.config(cursor="cross")
        self.__canvas.bind("<ButtonPress-1>",self.startRectangle)
        self.__canvas.bind("<B1-Motion>", self.growRectangle)
        self.__canvas.bind("<ButtonRelease-1>",lambda event: self.cropEnd(event,img))
        self.__root.bind("<Escape>",self.stopCrop)
        self.__shape=self.__canvas.create_rectangle
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
        self.__trainButton=Button(self.__root, text="Train Network", command=self.trainNetwork,anchor="e")
        self.__trainButton.grid(column=1,row=1,pady=10,padx=2)
        self.__antiIco=ImageTk.PhotoImage(file="Icons/anticlockwise.ico")
        self.__antiRotate=Button(self.__root,image=self.__antiIco,command=lambda: self.imageRotate(False,img),anchor="e")
        self.__antiRotate.grid(column=17,row=1,padx=2,pady=10)
        self.__clockwiseIco=ImageTk.PhotoImage(file="Icons/clockwise.ico")
        self.__clockRotate=Button(self.__root, image=self.__clockwiseIco,command=lambda: self.imageRotate(True,img),anchor="e")
        self.__clockRotate.grid(column=18,row=1,padx=2,pady=10)
        self.__cropIco=ImageTk.PhotoImage(file="Icons/crop.ico")
        self.__cropButton=Button(self.__root, image=self.__cropIco,command=lambda: self.crop(x,y,img),anchor="e")
        self.__cropButton.grid(column=19,row=1,padx=2,pady=10)
        self.__textScan=Button(self.__root,)
        if init==True:
            self.__antiRotate.config(state=DISABLED)
            self.__clockRotate.config(state=DISABLED)
            #self.__cropButton.config(state=DISABLED)
instance=GUI(Tk())
    