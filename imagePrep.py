from imutils.object_detection import non_max_suppression
import numpy as np, cv2, os, math,random
from PIL import Image, ImageFilter
os.chdir(os.path.dirname(os.path.realpath(__file__)))#Sets the path to be where the file is incase it isn't already there 
def textDetection(image):
	image = cv2.imread(image)#load the input image and get the image dimensions
	orig = image.copy() #Copies the image 
	(H, W) = image.shape[:2]
	layerNames = ["feature_fusion/Conv_7/Sigmoid","feature_fusion/concat_3"] #gets the two layers we need
	net = cv2.dnn.readNet("east_text_detection.pb")#Load the pre-trained EAST text detector
	blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),(123.68, 116.78, 103.94), swapRB=True, crop=False)#Creates a blob (collection of binary data) from the image
	net.setInput(blob)
	(scores, geometry) = net.forward(layerNames)#Puts it into the network with the layer names
	(numRows, numCols) = scores.shape[2:4] #gets the number of rows and columns
	boundBox=[]
	confidences=[]
	for y in range(0,numRows):
		scoresData=scores[0,0,y] #Gets tbe scores
		xData0=geometry[0,0,y]
		xData1=geometry[0,1,y]
		xData2=geometry[0,2,y]
		xData3=geometry[0,3,y]
		anglesData=geometry[0,4,y] #Gets geometry needed to make bounding boxes
		for x in range(0, numCols):
			if scoresData[x]<0.2:
				continue#If the score doesn't meet the minimum confidence, ignore
			(offsetX,offsetY)=(x*4.0,y*4.0)#Gets the offset factor (to account for size)
			angle=anglesData[x]
			cos=np.cos(angle)
			sin=np.sin(angle) #Calculate the rotation angles if any
			h=xData0[x]+xData2[x] #Get width and height of bounding box
			w=xData1[x]+xData3[x]
			endX=int(offsetX+(cos*xData1[x])+(sin*xData2[x]))
			endY=int(offsetY-(sin*xData1[x])+(cos*xData2[x]))
			startX=int(endX-w)
			startY=int(endY-h) #Get the start and end co-ords
			boundBox.append((startX,startY,endX,endY))
			confidences.append(scoresData[x])
	finalBoxes = non_max_suppression(np.array(boundBox), probs=confidences) #Finds bounding boxes that are weak and/or overlapping and removes them using non max suppression
	return finalBoxes
def thresholdImage(image):
    image=cv2.imread(image,0)
    blurred=cv2.GaussianBlur(image, (3,3),0) #Blurs the image to remove noise
    x,thresholded=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#Thresholds the image using Otsu's method and binary thresholding
    return thresholded
def characterSegment(image):
	orig=cv2.imread(image,0)
	contours,hierarchy=cv2.findContours(orig.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #Finds the countours in the image
	sortedConts=sorted(contours,key=lambda ctr: cv2.boundingRect(ctr)[0]) #Creates boundaries where there are significant gaps
	charlist=[]
	for i, ctr in enumerate(sortedConts):
		x,y,w,h=cv2.boundingRect(ctr)#Creates a list of the bounding boxes for the characters
		charlist.append(orig[y:y+h,x:x+w]) #'crops' the image arrays
	return charlist #Adds the character images to a list
def fitImage(image,black):
	x,y=image.size
	while x>40 or y>40:
		x,y=(i/1.05 for i in (x,y))
	while x<40 or y<40:
		if any((i*1.05>40 for i in (x,y))):
			break
		else:
			x,y=(i*1.05 for i in (x,y)) #Checks the size of the image and either enlarges it or shrinks it to fit
	x,y=(int(math.floor(i)) for i in (x,y))
	image=image.resize((x,y),Image.LANCZOS).convert("RGBA")
	if black:
		img=Image.new("1",(40,40),0)
	else:
		img=Image.new("1",(40,40),1)
	offset=((40-x)//2,(40-y)//2)
	img.paste(image,offset) #Puts the image in the centre of a 40x40 black canvas
	img.filter(ImageFilter.SMOOTH_MORE)#Smooths the image a bit 
	return img