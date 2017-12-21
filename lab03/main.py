import os
from scipy.io import wavfile as wav
from pylab import *
from scipy import *

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
    box = int(1/freq*ratio)
    total = 0
    
    maxRange = max(0, int(len(data) / box / 2 - (TS / 2 * freq)))
    minRange = min(int(len(data)/box)-2, int(len(data)/box/2+(TS/2*freq)))
    
    for i in range(maxRange, minRange):
        list1 = data[int(i*box):int((i+1)*box-1)]
        list2 = data[int((i+1)*box):int((i+2)*box-1)]
        var = 0
        
        for x,y in zip(list1, list2):
            var += abs(int(x)-int(y))
        total += var
    
    return total 

if __name__ == "__main__":
    dirs = os.listdir("train")
    for wavFile in dirs:
        print("processing: ", wavFile)
        rate, data = wav.read("train/" + wavFile)
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
    print(manTrue)
    print(manFalse)
    print(womanTrue)
    print(womanFalse)
    wsp = (manTrue + womanTrue) / sum(manTrue, manFalse, womanTrue, womanFalse)
    print(wsp)
        
        
        
