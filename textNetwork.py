#tensorFlowImages
import tensorflow as tf, numpy as np, os, pathlib,random
from PIL import Image
os.chdir(os.path.dirname(os.path.realpath(__file__)))
def trainModel(epochs,batchSize,hiddenLayers,layerSize,filename):
   dict={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, 'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61}
   data,labels,testdata,testlabels=[],[],[],[]
   for i in os.listdir("Chars74KResized"):
      x=random.sample(range(0,1016),6)
      dir=os.listdir("Chars74KResized/"+i)
      for j in dir:
           im=Image.open("Chars74KResized/"+i+"/"+j)
           if dir.index(j) in x:
               testdata.append(np.asarray(im))
               testlabels.append(dict[i])
           else:
               data.append(np.asarray(im))
               labels.append(dict[i])
   #lr_schedule = tf.keras.optimizers.schedules.InverseTimeDecay(0.001,decay_steps=(len(labels)/batchSize)*1000,decay_rate=1,staircase=False)
   #optimiser=tf.keras.optimizers.Adam(tf.keras.optimizers.schedules.InverseTimeDecay(0.001,decay_steps=4922,decay_rate=0.5,staircase=False))
   c = list(zip(data, labels))
   random.shuffle(c)
   data, labels = zip(*c)
   data,labels=np.asarray(data,dtype=np.float32),np.asarray(labels)
   data=data/255.0
   c = list(zip(testdata, testlabels))
   random.shuffle(c)
   testdata, testlabels = zip(*c)
   testdata,testlabels=np.asarray(testdata,dtype=np.float32),np.asarray(testlabels)
   testdata=testdata/255.0
   data = data.reshape((data.shape[0], data.shape[1], data.shape[2], 1))
   testdata = testdata.reshape((testdata.shape[0], testdata.shape[1], testdata.shape[2], 1))
   inputShape=data.shape[1:]
   earlystop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
   model = tf.keras.models.Sequential()
   model.add(tf.keras.layers.BatchNormalization())
   model.add(tf.keras.layers.Conv2D(16, (3,3), activation='relu', kernel_initializer='he_uniform', input_shape=inputShape))
   model.add(tf.keras.layers.MaxPooling2D((2, 2)))
   model.add(tf.keras.layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_uniform', input_shape=inputShape))
   model.add(tf.keras.layers.MaxPooling2D((2, 2)))
   model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
   model.add(tf.keras.layers.Flatten())
   model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu'))
   model.add(tf.keras.layers.Flatten())
   for i in range (0,hiddenLayers):
     model.add( tf.keras.layers.Dense(layerSize, activation='relu'))
   model.add(tf.keras.layers.Dense(62, activation='softmax'))
   model.compile(optimizer="SGD",loss='sparse_categorical_crossentropy',metrics=['accuracy'])
   model.fit(data, labels, epochs=epochs,batch_size=batchSize,validation_data=(testdata,testlabels),shuffle="batch",steps_per_epoch=None,verbose=1,use_multiprocessing=True,callbacks=earlystop)
   model.evaluate(testdata,  testlabels, verbose=2)
   model.save("models/"+filename+".h5")g
def getPredict(filename,image):
    model=tf.keras.models.load_model("models/"+filename+".h5")
    reverseDict={0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z', 36: 'a', 37: 'b', 38: 'c', 39: 'd', 40: 'e', 41: 'f', 42: 'g', 43: 'h', 44: 'i', 45: 'j', 46: 'k', 47: 'l', 48: 'm', 49: 'n', 50: 'o', 51: 'p', 52: 'q', 53: 'r', 54: 's', 55: 't', 56: 'u', 57: 'v', 58: 'w', 59: 'x', 60: 'y', 61: 'z'}
    results=model.predict_classes(image,verbose=0)
    endstr="".join([reverseDict[i] for i in results])
    return endstr
#trainModel(20,32,1,128,"default_model")    
