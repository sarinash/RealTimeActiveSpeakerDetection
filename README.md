# RealTimeActiveSpeakerDetection
Train a model with an audio file from the speaker and the detect the speaker in real time.

___
## Overview

![makingTrainingData](https://user-images.githubusercontent.com/60202851/101612904-82211b80-3a4e-11eb-9e0a-e835cbd60dfa.JPG)
![TrainingModelResults](https://user-images.githubusercontent.com/60202851/101612909-83eadf00-3a4e-11eb-8f43-b5fb1652ea51.jpg)


___

### Dependencies:
* pip install numpy
* pip install pandas
* pip install tensorflow
* pip install keras
* pip install librosa



### How it works:
_ First record your audio for 30 seconds using recordaudio.py (you can skip this part and just use a pre recorded file)
_ Make a training data using maketrainingdata.py as data_10.json
_ Train a model out of your voice using training.py and save the model as model.h5
_ Run the Speaker.py


