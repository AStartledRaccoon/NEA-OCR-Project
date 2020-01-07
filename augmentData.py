#DataAugment
import os, cv2, numpy as np
from skimage.util import random_noise
os.chdir(os.path.dirname(os.path.realpath(__file__)))
dir=sorted(os.listdir("Chars74KResized/"))
os.mkdir("Chars74KAugment")
for i in dir:
    os.mkdir("Chars74KAugment/"+i)
    for j in os.listdir("Chars74KResized/"+i):
        img=cv2.imread("Chars74KResized/"+i+"/"+j,0)
        img = random_noise(img, mode='s&p',amount=0.015)
        img = np.array(255*img, dtype = 'uint8')
        gauss=np.random.normal(0,0.5,img.size)
        gauss=gauss.reshape(img.shape[0],img.shape[1]).astype("uint8")
        noise=img+img*gauss
        x,thresholded=cv2.threshold(noise,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #cv2.imshow("noisy",thresholded)
        #cv2.waitKey(0)
        cv2.imwrite("Chars74KAugment/"+i+"/augment"+j, thresholded)
