#renamefile.py
import os
dir=os.path.dirname(os.path.realpath(__file__))+"/Chars74K/"

for i in os.listdir(dir):
    os.rename(dir+i,dir+i.replace("Char ",""))