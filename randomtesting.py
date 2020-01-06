import os, imagePrep, random, numpy as np
from PIL import ImageOps, Image, ImageEnhance
from statistics import mode
os.chdir(os.path.dirname(os.path.realpath(__file__)))
dir=os.listdir("NaturalImages/")
origImages=[]
finalimages=[]
for i in dir:
    for j in os.listdir("NaturalImages/"+i+"/"):
        im = Image.open("NaturalImages/"+i+"/"+j).convert('LA')
        enhancer = ImageEnhance.Contrast(im)
        enhanced_im = enhancer.enhance(10)
        enhanced_im.save("tmp/tmp7.png")
        origImages.append(enhanced_im)
        x=imagePrep.thresholdImage("tmp/tmp7.png")
        counts=np.argmax(np.bincount(np.ndarray.flatten(x)))
        if counts!=0:
            a=imagePrep.fitImage(ImageOps.invert(Image.fromarray(x)),True)
            finalimages.append([a,i])
        else:
            a=imagePrep.fitImage(ImageOps.invert(Image.fromarray(x)),False)
            a=a.convert('L')
            a=ImageOps.invert(a)
            a=a.convert('1')
            finalimages.append([a,i])
#x=-1
#for i in finalimages:
    #x+=1
    #i[0].save("Chars74KResized/"+i[1]+"/img"+str(x)+".png")