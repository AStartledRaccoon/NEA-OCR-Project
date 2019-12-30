#tensorFlowImages
import tensorflow as tf, numpy as np, os, pathlib,random
from PIL import Image
os.chdir(os.path.dirname(os.path.realpath(__file__)))
def trainModel(epochs,batchSize,hiddenLayers,layerSize,filename):
   dict={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, 'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61}
   data,labels=[],[]
   for i in os.listdir("Chars74KResized"):
     for j in os.listdir("Chars74KResized/"+i):
           im=Image.open("Chars74KResized/"+i+"/"+j)
           data.append(np.asarray(im))
           labels.append(dict[i])
   c = list(zip(data, labels))
   random.shuffle(c)
   data, labels = zip(*c)
   data,labels=np.asarray(data,dtype=np.float32),np.asarray(labels)
   model = tf.keras.models.Sequential()
   model.add(tf.keras.layers.Flatten(input_shape=(40, 40)))
   for i in range (0,hiddenLayers):
     model.add( tf.keras.layers.Dense(layerSize, activation='relu'))
   model.add(tf.keras.layers.Dense(62, activation='softmax'))
   model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
   model.fit(data, labels, epochs=epochs,batch_size=batchSize,shuffle=True,steps_per_epoch=450,verbose=1,use_multiprocessing=True)
   model.save("models/"+filename+".h5")
def getPredict(filename,image):
    model=tf.keras.models.load_model("models/"+filename+".h5")
    reverseDict={0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z', 36: 'a', 37: 'b', 38: 'c', 39: 'd', 40: 'e', 41: 'f', 42: 'g', 43: 'h', 44: 'i', 45: 'j', 46: 'k', 47: 'l', 48: 'm', 49: 'n', 50: 'o', 51: 'p', 52: 'q', 53: 'r', 54: 's', 55: 't', 56: 'u', 57: 'v', 58: 'w', 59: 'x', 60: 'y', 61: 'z'}
    results=model.predict_classes(image,verbose=0)
    endstr="".join([reverseDict[i] for i in results])
    return endstr
trainModel(1000,64,7,1129,"default_model")
    
    