# NEA Program for OCR
### Prerequisites ###
* Python 3
* Pip
* OpenCV (3.4.2 or above)
* PIL
* NumPy
* scikit-image
* scikit-learn
* TensorFlow (version 2.x)
* imutils
### Installation Instructions ###
#### Pip ####
##### Windows #####
1. Download get-pip.py from https://bootstrap.pypa.io/get-pip.py
2. Open a command prompt and go to to the folder you installed get-pip.py to 
3. Run the command `python get-pip.py`
4. (Optional) Verify that pip is installed by running the command `pip -V`

##### Ubuntu 18.04 #####
1. Update the package list with `sudo apt update`
2. Install pip for Python 3 with `sudo apt install python3-pip`
3. (Optional) check the installation with `pip3 --version`

#### PIL #####
1. Open a command prompt
2. Run the command `pip install Pillow`

#### NumPy ####
1. Open a a command prompt
2. Run the command `pip install numpy`

#### OpenCV ####
1. Open a command prompt
2. Run the command `pip install opencv-contrib-python`

#### scikit-image ####
1. Open a command prompt
2. Run the command `pip install scikit-image`

#### scikit-learn ####
1. Open a command prompt
2. Run the command `pip install scikit-learn`

#### TensorFlow ####
1. Open a command prompt
2. Run the command `pip install tensorflow`

#### imutils ####
1. Open a command prompt
2. Run the command `pip install imutils`


### Aims ###
- [x] Ability to train the neural network
    - [x] Take each pixel and get its brightness (I.e. how close the value is to white) 
    - [x] Assign each of these to a neuron 
    - [x] Send it through a certain number of hidden layers, each with another certain number of neurons (need to research how many I should use) 
    - [x] Once it's gone through these layers, it goes to the final layer, with a neuron for each character 
- [ ] An easily understandable, clear and simple GUI containing: 
    - [ ] An info sheet in html that opens in the user's default html viewer 
    - [x] User can upload photos of printed text to be scanned (in PNG or JPEG format) with an upload button that creates a file dialog
    - [x] Preview and crop photos before scanning 
    - [x] Rotate photos before scanning
    - [ ] Network settings and custom training
    - [ ] Ability to view the output and save it in a different format if the user wishes
- [x] Detect, isolate and prepare text in an image to be sent into the network
    - [x] Text detection
    - [x] Character segmentation
    - [x] Threshold character image and other preparation means