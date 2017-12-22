import os
import numpy as np
from pylab import *
from scipy import *
from scipy.io import wavfile as wav
import types

TS = 3

maleFemaleFreq = [120, 232]

voiceMan = [85, 180]
voiceWoman = [165,255]

manTrue = 0
manFalse = 0

womanTrue = 0
womanFalse = 0

def simpleRecognition(rate, data):
    if(checkBaseFreq(maleFemaleFreq[0], rate, data) < checkBaseFreq(maleFemaleFreq[1], rate, data)): 
        return 1
    else:
        return 0

def checkBaseFreq(freq, ratio, data):
    frame = int(1/freq*ratio)
    total = 0
    
    #maxRange = max(0, int(len(data) / frame / 2 - (TS / 2 * freq)))
    maxRange =  int(len(data) / frame / 2)
    #minRange = min(int(len(data)/frame)-2, int(len(data)/frame/2+(TS/2*freq)))
    minRange = int(len(data)/frame)
    
    for i in range(maxRange, minRange):
        list1 = data[int(i*frame):int((i+1)*frame-1)]
        list2 = data[int((i+1)*frame):int((i+2)*frame-1)]
        var = 0
        
        for x,y in zip(list1, list2):
            if type(x) is np.ndarray:
                x = x[0]
            if type(y) is np.ndarray:
                y = y[0]
            x = int(x) 
            y = int(y)
            var += abs(x-y)
        
        total += var
    
    return total

if __name__ == "__main__":
    dirs = os.listdir("train")
    for wavFile in dirs:
        print("Open: ", wavFile)
        rate, data = wav.read("train/" + wavFile)
        print("Processing: ", wavFile)
        gender = wavFile.split('_')[1].split('.')[0]
        found = simpleRecognition(rate, data)
        if(found == 1):
            found = 'M'
        else:
            found = 'K'
        
        if(found == gender):
            if(gender == 'M'):
                manTrue += 1
            if(gender == 'K'):
                womanTrue += 1
        else:
            if(gender == 'M'):
                manFalse += 1
            if(gender == 'K'):
                womanFalse += 1
    print('MAN_TRUE: ',manTrue)
    print('MAN_FALSE: ',manFalse)
    print('WOMAN_TRUE: ',womanTrue)
    print('WOMAN_FALSE: ',womanFalse)
    wsp = (manTrue + womanTrue) / sum(manTrue, manFalse, womanTrue, womanFalse)
    print('WSP: ',wsp)
        
        
        
