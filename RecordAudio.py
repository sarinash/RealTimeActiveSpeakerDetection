from threading import Timer
import sounddevice as sd
from scipy.io.wavfile import write
import os
fs = 44100  # this is the frequency sampling
seconds = 30  # Duration of recording
n=0 # iteration for number of recordings

def getAudio():

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print("Speak")
    sd.wait()  # Wait until 5 seconds
    #print("finished")
    global n
    n+=1
    write('C:/Users/sarina/Desktop/sounds/test/tes/output'f"{n}"'.wav', fs, myrecording)  # Save as WAV file

    Timer(30, getAudio).start()

getAudio()