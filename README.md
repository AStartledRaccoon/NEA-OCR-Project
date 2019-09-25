# NEA Program for OCR
### Prerequisites ###
* PIL (pip install PIL)
* OpenCV (pip install opencv-contrib-python)

### Aims ###
- [ ] Ability to train the neural network, this will be hidden from the end user but is necessary 
    - [ ] Take each pixel and get its brightness (I.e. how close the value is to white) 
    - [ ] Assign each of these to a neuron 
    - [ ] Send it through a certain number of hidden layers, each with another certain number of neurons (need to research how many I should use) 
    - [ ] Once it's gone through these layers, it goes to the final layer, with a neuron for each character 
- [ ] An easily understandable, clear and simple GUI containing: 
    - [ ] An info sheet in html that opens in the user's default html viewer 
    - [x] User can upload photos of printed text to be scanned (in PNG or JPEG format) with an upload button that creates a file dialog 
    - [ ] Preview and crop photos before scanning 
    - [x] Rotate photos before scanning
    - [ ] Ability to view the output and save it in a different format if the user wishes
- [ ] Detect, isolate and prepare text in an image to be sent into the network
    - [ ] Text detection
    - [ ] Character segmentation
    - [ ] Threshold character image and other preparation means