#tensorFlowImages
import tensorflow as tf, numpy as np, os, pathlib
from PIL import Image
os.chdir(os.path.dirname(os.path.realpath(__file__)))
AUTOTUNE=tf.data.experimental.AUTOTUNE #Creates an easy to use version fo the autotune 
data_dir=pathlib.Path("Chars74KResized")
image_count=len(list(data_dir.glob('*/*.png'))) #Counts all the images 
list_data=tf.data.Dataset.list_files(str(data_dir/"*/*")) #Finds all the files
letters=np.array([item.name for item in data_dir.glob('*')]) #Gets the letters (directory names)
batchSize=32 #Sets batch size (batches that are fed into network)
imgHeight=40
imgWidth=40 #Image dimensions
stepsPerEpoch=np.ceil(image_count/batchSize)
def labelFromPath(file_path):
    parts=tf.strings.split(file_path, os.path.sep)
    label=parts[-2]==letters #Gets the labels
    img=tf.io.read_file(file_path)
    img=tf.image.decode_png(img, channels=3)
    img=tf.image.convert_image_dtype(img,tf.float32)  #Converts the image to a form tensorflow can read
    return img, label 
labeled_ds=list_ds.map(labelFromPath,num_parallel_calls=AUTOTUNE) #Creates a map that tensorflow can read
def trainingPrep(ds, cache=True,shuffle_buffer_size=1000):
    if cache:
        if isinstance(cache,str):
            ds=ds.cache(cache) #Caches data to save time
        else:
            ds=ds.cache()
    data=data.shuffle(buffer_size=shuffle_buffer_size)
    data=data.repeat()
    data=data.batch(batchSize) #Correctly shuffles the data and puts it into batches
    return data
train_data=trainingPrep(labeled_data)
image_batch,label_batch=next(iter(train_data))
learning_rate=0.5
epochs=5 #The number of full cycles throught the training data
x=tf.placeholder(tf.float32,[None,1600])
y=tf.placeholder(tf.float32,[None,62])
#Having 4 hidden layers due to formula (will add to word document) 
#Decrease by about 250 nodes per layer? Will have to research size of hidden layers
W1=tf.Variable(tf.random_normal([1600,1350],stddev=0.03),name="W1")
B1=tf.Variable(tf.randm_normal([1350]),name="B1")
W2=tf.Variable(tf.random_normal([1350,1100],stddev=0.03),name="W2")
B2=tf.Variable(tf.randm_normal([1100]),name="B2")
W3=tf.Variable(tf.random_normal([1100,850],stddev=0.03),name="W3")
B3=tf.Variable(tf.randm_normal([850]),name="B3")
W4=tf.Variable(tf.random_normal([850,600],stddev=0.03),name="W4")
B4=tf.Variable(tf.randm_normal([600]),name="B4")
W5=tf.Variable(tf.random_normal([600,350],stddev=0.03),name="W5")
B5=tf.Variable(tf.randm_normal([350]),name="B5")
W6=tf.Variable(tf.random_normal([350,100],stddev=0.03),name="W6")
B6=tf.Variable(tf.randm_normal([100]),name="B6")#
W7=tf.Variable(tf.random_normal([100,62],stddev=0.03),name="W7")
B7=tf.Variable(tf.randm_normal([62]),name="B7")
#Crreates random biases and weights