# NEA Program for OCR
### Prerequisites ###
* Python
* Pip
* OpenCV
* PIL
* scikit-image
* scikit-learn
* TensorFlow (version 1.x)
### Installation Instructions ###
#### Windows ####
##### Pip #####
1. Download get-pip.py from https://bootstrap.pypa.io/get-pip.py
2. Open a command prompt and go to to the folder you installed get-pip.py to 
3. Run the command `python get-pip.py`
4. (Optional) Verify that pip is installed by running the command `pip -V`

##### PIL ######
1. Open a command prompt
2. Run the command `pip install Pillow`

##### Numpy #####
1. Open a a command prompt
2. Run the command `pip install numpy`

##### OpenCV #####
1. Open a command prompt
2. Run the command `pip install opencv-contrib-python`

##### scikit-image #####
1. Open a command prompt
2. Run the command `pip install scikit-image`

##### scikit-learn #####
1. Open a command prompt
2. Run the command `pip install scikit-learn`

##### TensorFlow #####
1. Open a command prompt
2. Run the command `pip install tensorflow`


### Aims ###
- [ ] Ability to train the neural network, this will be hidden from the end user but is necessary 
    - [x] Take each pixel and get its brightness (I.e. how close the value is to white) 
    - [ ] Assign each of these to a neuron 
    - [ ] Send it through a certain number of hidden layers, each with another certain number of neurons (need to research how many I should use) 
    - [ ] Once it's gone through these layers, it goes to the final layer, with a neuron for each character 
- [ ] An easily understandable, clear and simple GUI containing: 
    - [ ] An info sheet in html that opens in the user's default html viewer 
    - [x] User can upload photos of printed text to be scanned (in PNG or JPEG format) with an upload button that creates a file dialog 
    - [x] Preview and crop photos before scanning 
    - [x] Rotate photos before scanning
    - [ ] Ability to view the output and save it in a different format if the user wishes
- [x] Detect, isolate and prepare text in an image to be sent into the network
    - [x] Text detection
    - [x] Character segmentation
    - [x] Threshold character image and other preparation means