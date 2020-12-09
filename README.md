# RealTimeActiveSpeakerDetection
Train a model with an audio file from the speaker and the detect the speaker in real time.

___
## Overview




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


