import os
from pylab import *
from scipy import *
from scipy.io import wavfile as wav
from scipy.signal import hamming
import numpy as np

FreqMaleFemale = [120, 232]
HumanVoiceMax = [60, 160]

ManTrue = 0
ManFalse = 0

WomanTrue = 0
WomanFalse = 0



if __name__ == "__main__":
    dirs = os.listdir("train")
    for wavFile in dirs:
        rate, data = wav.read("train/" + wavFile)
        data = data.astype(float) / 2**16 # normalize to -1 to 1
        data = data[:0] + data[:1] # sereo to mono
        
        gender = wavFile.split('_')[1].split('.')[0]
        found = HarmonicProductSpectrum(rate, data)
        
        if(found == 1):
            found = 'M'
        else:
            found = 'K'
        
        if(found == gender):
            if(gender == 'M'):
                ManTrue += 1
            if(gender == 'K'):
                WomanTrue += 1
        else:
            if(gender == 'M'):
                ManFalse += 1
            if(gender == 'K'):
                WomanFalse += 1
                
    print(ManTrue)
    print(ManFalse)
    print(WomanTrue)
    print(WomanFalse)
