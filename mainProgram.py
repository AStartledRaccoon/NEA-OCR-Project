#main program space
#Callum Cafferty
#NEA
import os, imagePrep
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageOps
class GUI(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.__root=master
        self.__root.title("OCR AI")
        self.grid()
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        blankimg=Image.open("transparent.png")
        self.mainWindow(595,842,blankimg,True) #Sets up the main window  with a placeholder image
        self.__root.mainloop()
    def imageDialog(self):
        self.__filename=filedialog.askopenfilename(initialdir=os.path.expanduser('~/Pictures'),title="Select file",filetypes=(("Images","*.png *.jpg"),("PNG Images","*.png"),("JPEG Images","*.jpg"),("All files","*.*")))
        self.__userimg=Image.open(self.__filename)
        self.addImage(self.__userimg) #Gives the user a file dialog to upload the image
    def addImage(self,img):
        imgsize=img.size
        while imgsize[0]>1600 or imgsize[1]>900:
            imgsize=[int(i//1.05) for i in imgsize]
            img=img.resize(imgsize,Image.LANCZOS)
        imgsize=[round(i/32)*32 for i in imgsize]
        img=img.resize(imgsize,Image.LANCZOS) #Resizes the image to be less than 1600x900
        self.mainWindow(*img.size,img,False) #Reforms the main window
    def imageRotate(self, clockwise, img):
        if clockwise==True:
            self.addImage(img.rotate(270,expand=1))
        else:
            self.addImage(img.rotate(90,expand=1)) #Rotates the image then passes it to the addImage subroutine for resizing
    def trainNetwork(self):
            pass
    def cancelCrop(self):
        self.__cropConfirm.destroy()
        self.__canvas.delete(self.__drawn)
        self.__cropButton.config(state="normal") #Removes the rectangle and returns the crop button to its normal state
    def doCrop(self, event,img):
        self.__canvas.delete(self.__drawn)
        self.__cropConfirm.destroy()
        self.__cropImg=img.crop((self.__start.x, self.__start.y, event.x, event.y))
        self.__cropButton.config(state="normal")#Returns the image back to normal
        self.addImage(self.__cropImg) #Crops the image based on the user's crop and then passes the cropped image to addImage
    def cropEnd(self, event,img):
        self.__cropConfirm=Toplevel(self.__root)
        self.__cropConfirm.title("Crop")
        self.__canvas.config(cursor="")
        self.__canvas.unbind("<ButtonPress-1>")
        self.__canvas.unbind("<B1-Motion>")
        self.__canvas.unbind("<ButtonRelease-1>") 
        self.__cropButtonA=Button(self.__cropConfirm,text="Confirm",command=lambda: self.doCrop(event,img))
        self.__cancelButton=Button(self.__cropConfirm,text="Cancel",command=self.cancelCrop)#Gives the user the option of cancelling their crop or continuing with it
        self.__cropLabel=Label(self.__cropConfirm, text="Crop selection?").grid(row=0, column=0, columnspan=2, padx=3, pady=3)
        self.__cropButtonA.grid(row=1, column=0, padx=3, pady=3)
        self.__cancelButton.grid(row=1, column=1, padx=3, pady=3)
        self.__cropConfirm.grid()
    def growRectangle(self,event):
        self.__canvas = event.widget
        if self.__drawn: self.__canvas.delete(self.__drawn)
        objectId = self.__shape(self.__start.x, self.__start.y, event.x, event.y,fill="gray50", stipple="gray50")
        self.__drawn = objectId #Draws the cropping box for every time it grows
    def startRectangle(self,event):
        self.__start=event
        self.__drawn=None #Event handler for starting a crop
    def stopCrop(self,event):
        self.__canvas.unbind("<ButtonPress-1>")
        self.__canvas.unbind("<B1-Motion>")
        self.__canvas.unbind("<ButtonRelease-1>")
        self.__cropButton.config(state="normal") #Event handling for cancelling the crop
    def crop(self,x,y,img):
        self.__cropButton.config(state=DISABLED)
        self.__canvas.config(cursor="cross") #Changes the cursor to a cross
        self.__canvas.bind("<ButtonPress-1>",self.startRectangle)
        self.__canvas.bind("<B1-Motion>", self.growRectangle)
        self.__canvas.bind("<ButtonRelease-1>",lambda event: self.cropEnd(event,img))
        self.__root.bind("<Escape>",self.stopCrop) 
        self.__shape=self.__canvas.create_rectangle #Starts the cropping process
    def textScan(self):
        self.__img.save("tmp/temp.png")
        coordslist=imagePrep.textDetection("tmp/temp.png")#Runs the image through the textDetection
        imagesList,threshedList,characterlist,resizedList=[],[],[],[]
        for i in coordslist:
            imagesList.append(self.__img.crop(i)) #Makes a list of each image of words as returned by textDetection
        for x in imagesList:
            x.save("tmp/temp2.png")
            threshedList.append(ImageOps.invert(Image.fromarray(imagePrep.thresholdImage("tmp/temp2.png")))) #Creates a list of thresholded images
        for x in threshedList:
            x.save("tmp/temp2.png")
            characterlist.append([Image.fromarray(i) for i in imagePrep.characterSegment("tmp/temp2.png")]) #Creates a lst of segmented character images
        for x in characterlist:
            resizedList.append([imagePrep.fitImage(i) for i in x]) #Creates a list of the resized characters
    def mainWindow(self,x,y,img,init):
        if init==False:
            self.__canvas.grid_forget()
            self.__canvas.delete("all")
        self.__img=img
        self.__imgdisplay=ImageTk.PhotoImage(img)
        self.__canvas=Canvas(self.__root,width=x,height=y,highlightthickness=1, highlightbackground="black")
        self.__canvas.grid(row=0,padx=20,pady=10,columnspan=21)
        self.__canvas.create_image(0,0,image=self.__imgdisplay,anchor="nw")#Adds the image to the canvas
        self.__imageButton=Button(self.__root, text="Import Image", command=self.imageDialog,anchor="e")
        self.__imageButton.grid(column=0,row=1,pady=10,padx=2)
        self.__trainButton=Button(self.__root, text="Train Network", command=self.trainNetwork,anchor="e")
        self.__trainButton.grid(column=1,row=1,pady=10,padx=2) #Create the two text buttons on the left
        self.__antiIco=ImageTk.PhotoImage(file="Icons/anticlockwise.ico")
        self.__antiRotate=Button(self.__root,image=self.__antiIco,command=lambda: self.imageRotate(False,img),anchor="w")
        self.__antiRotate.grid(column=17,row=1,padx=2,pady=10)
        self.__clockwiseIco=ImageTk.PhotoImage(file="Icons/clockwise.ico")
        self.__clockRotate=Button(self.__root, image=self.__clockwiseIco,command=lambda: self.imageRotate(True,img),anchor="w")
        self.__clockRotate.grid(column=18,row=1,padx=2,pady=10)
        self.__cropIco=ImageTk.PhotoImage(file="Icons/crop.ico")
        self.__cropButton=Button(self.__root, image=self.__cropIco,command=lambda: self.crop(x,y,img),anchor="w")
        self.__cropButton.grid(column=19,row=1,padx=2,pady=10)
        self.__scanIco=ImageTk.PhotoImage(Image.open("Icons/scan.ico").resize((32,32),Image.ANTIALIAS).convert("RGBA")) #Resizes the scan icon
        self.__scanButton=Button(self.__root, image=self.__scanIco, command=self.textScan, anchor="w")
        self.__scanButton.grid(column=20, row=1, padx=2, pady=10) #Creates all the icons and their respective bbuttons
        if init==True:
            self.__antiRotate.config(state=DISABLED)
            self.__clockRotate.config(state=DISABLED)
            self.__cropButton.config(state=DISABLED)
            self.__scanButton.config(state=DISABLED) #Disables the buttons if the user hasn't loaded an iamge yet 

instance=GUI(Tk())
    