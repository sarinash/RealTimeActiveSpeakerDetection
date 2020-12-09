from threading import Timer
import requests, urllib, json, time, threading
import sounddevice as sd
from scipy.io.wavfile import write
from tensorflow import keras
import json
import numpy as np
import os
import os
import math
import librosa
# Variable for keeping time range of the current/previous time window in the correlation array.
iHead = 0
iTail = 0
# iHead_prev = 0
# iTail_prev = 0
tWinHead = time.time()

# duration of the time window to average correlaiton
durWin = 5

fs = 44100  # this is the frequency sampling
seconds = 5  # Duration of recording
n = 0  # iteration for number of recordings
m = 0  # iteration for mfcc decoding

A = 0  # person A talking time
B = 0  # person B talking time
C = 0  # no one is talking
SAMPLE_RATE = 44100
TRACK_DURATION = 5  # measured in seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION
model = keras.models.load_model("model.h5")  # saved training model


##################################################################################################################################################
def getAudio():  # save audio every five seconds
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    # print("Speak")
    sd.wait()  # Wait until 5 seconds
    # print("finished")
    global n
    n += 1
    write('C:/Users/sarina/Desktop/sounds/test/tes/output'f"{n}"'.wav', fs, myrecording)  # Save as WAV file
    Timer(5, getAudio).start()  # five is also for the duration of recording


##################################################################################################################################################
def save_mfcc(num_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):  # get the mfcc of the real-time audio
    # dictionary to store mapping, labels, and MFCCs
    Timer(5, save_mfcc().start())
    global n
    data = {
        "mfcc": []
    }

    samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)

    # loop through all genre sub-folder
    signal, sample_rate = librosa.load('C:/Users/sarina/Desktop/sounds/test/tes/output'f"{n}"'.wav', sr=SAMPLE_RATE)

    # process all segments of audio file
    for d in range(num_segments):
        # calculate start and finish sample for current segment
        start = samples_per_segment * d
        finish = start + samples_per_segment
        # extract mfcc
        mfcc = librosa.feature.mfcc(signal[start:finish], sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
                                    hop_length=hop_length)
        mfcc = mfcc.T

        # store only mfcc feature with expected number of vectors
        if len(mfcc) == num_mfcc_vectors_per_segment:
            data["mfcc"].append(mfcc.tolist())
            print("{}, segment:{}".format('C:/Users/sarina/Desktop/sounds/test/tes/output'f"{n}"'.wav', d + 1))

    # save MFCCs to json file
    with open('test'f"{n}"'.json', "w") as fp:
        json.dump(data, fp, indent=4)




##########################################################################################################################################
def load_data():
    global n
    with open('test'f"{n}"'.json', "r") as fp:
        data = json.load(fp)

    # convert lists to numpy arrays
    X = np.array(data["mfcc"])
    # print("Data succesfully loaded!")
    Timer(5, load_data()).start()  # five is also for the duration of recording
    return X


getAudio()
save_mfcc()
X = load_data()
predict = model.predict(X)
print(predict)
A += (predict[9, 0])
B += (predict[9, 1])
C += (predict[9, 2])
print(A)
print(B)
print(C)
