#textrecognitionNetwork
import random, string,os
from PIL import Image, ImageFont, ImageDraw
os.chdir(os.path.dirname(os.path.realpath(__file__)))
def createImages():
    possibleChars=list(string.ascii_letters)+list(string.digits)#Gets a list of all possible choices
    randomLens=[random.randint(3,10) for i in range(0,10)]#Generates a list of possible lengths
    randStrings=["".join(random.sample(possibleChars,i)) for i in randomLens]#Generates random strings of lengths as listed before
    fonts=os.listdir("fonts/")
    imglist=[]
    for i in randStrings:
        font=ImageFont.truetype("fonts/"+random.choice(fonts),22)
        size=max(font.getsize(x) for x in randStrings)
        image=Image.new("RGB",size,"black")
        draw=ImageDraw.Draw(image)
        draw.text((0,0),i,(255,255,255),font=font)
        image.show()
createImages()