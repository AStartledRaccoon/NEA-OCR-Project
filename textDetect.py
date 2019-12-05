from imutils.object_detection import non_max_suppression
import numpy, cv2, os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
def textDetection(image):
	image = cv2.imread(image)#load the input image and grab the image dimensions
	orig = image.copy()
	(H, W) = image.shape[:2]
	layerNames = ["feature_fusion/Conv_7/Sigmoid","feature_fusion/concat_3"] #gets the two layers we need
	net = cv2.dnn.readNet("east_text_detection.pb")# load the pre-trained EAST text detector
	blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),(123.68, 116.78, 103.94), swapRB=True, crop=False)#Creates a blob (collection of binary data) from the image
	net.setInput(blob)
	(scores, geometry) = net.forward(layerNames)#Puts it into the network with the layer names
	(numRows, numCols) = scores.shape[2:4] #gets the number of rows and columns
	boundBox = []
	confidences = []
	for y in range(0, numRows):
		scoresData = scores[0, 0, y] #gets tbe scores
		xData0 = geometry[0, 0, y]
		xData1 = geometry[0, 1, y]
		xData2 = geometry[0, 2, y]
		xData3 = geometry[0, 3, y]
		anglesData = geometry[0, 4, y] #Gets geometry needed to make bounding boxes
		for x in range(0, numCols):
			if scoresData[x] < 0.2:
				continue #If the score doesn't meet the minimum confidence, ignore
			(offsetX, offsetY) = (x*4.0, y*4.0)#Gets the offset factor (to account for size)
			angle = anglesData[x]
			cos = numpy.cos(angle)
			sin = numpy.sin(angle) #Calculate the rotation angles
			h = xData0[x] + xData2[x] #Get width and height of bounding box
			w = xData1[x] + xData3[x]
			endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
			endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
			startX = int(endX - w)
			startY = int(endY - h) #Get the start and end co-ords
			boundBox.append((startX, startY, endX, endY))
			confidences.append(scoresData[x])
	finalBoxes = non_max_suppression(numpy.array(boundBox), probs=confidences) #Surpress weak/overlapping finalBoxes
	#for (startX, startY, endX, endY) in finalBoxes:
	#	cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2) #Add bounding boxes to the image
	return finalBoxes