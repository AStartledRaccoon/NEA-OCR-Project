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
    - [ ] An upload button that opens a file browser 
    - [ ] Preview window allowing the user to crop their image 
    - [ ] Ability to view the output and save it in a different format if the user wishes 
- [ ] User can upload photos of printed text to be scanned (in PNG or JPEG format) 
- [ ] Preview and crop photos before scanning 
- [ ] Find text, scan it and output it to a .txt file or alternatively export to a file of the user's choice 