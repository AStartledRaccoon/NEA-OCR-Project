import os
from PIL import Image, ImageOps
os.chdir(os.path.dirname(os.path.realpath(__file__)))
img=Image.open("transparent.png")
img=ImageOps.invert(img)
img.show()