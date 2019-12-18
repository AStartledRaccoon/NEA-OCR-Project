#A simple program to resize the Chars74K dataset to 40x40 images and invert the colours
import os
from PIL import Image, ImageOps
os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.mkdir("Chars74KResized") #Creates a new directory for the files
for i in os.listdir("Chars74K/"):
    os.mkdir("Chars74KResized/"+i)#Creates a new directory for each character
    for j in os.listdir("Chars74K/"+i):
        im=Image.open("Chars74K/"+i+"/"+j)
        im=ImageOps.invert(im) #Inverts the image
        im=im.resize((40,40)) #Resizes the image
        im.save("Chars74KResized/"+i+"/"+j)#Saves the image