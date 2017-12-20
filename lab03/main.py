import os
from scipy.io import wavfile as wav
from pylab import *
from scipy import *

FreqMaleFemale = [120, 232]
HumanVoiceMax = [60, 160]

ManTrue = 0
ManFalse = 0

WomanTrue = 0
WomanFalse = 0

#od tąd wymazujemy-----------
maleFemaleFreq = [120, 232]
TS=3 #time for simple method
humanVoiceMinMAx = [80,255]
maleMinMax=[60,160]
femaleMinMax=[180,270]
HPSLoop=5
#do tad-----------------------

def simpleRecognition(rate, data):
    if(checkBaseFreq(maleFemaleFreq[0], rate, data) < checkBaseFreq(maleFemaleFreq[1], rate, data)): 
        return 1
    return 0
    
def checkBaseFreq(freq, ratio, data):
    box = int(1/freq*ratio)
    return sum([listVariation(data[int(i*box):int((i+1)*box-1)],data[int((i+1)*box):int((i+2)*box-1)]) for i in range( max(0,int(len(data)/box/2-(TS/2*freq))), min(int(len(data)/box)-2,int(len(data)/box/2+(TS/2*freq))),1)])

def listVariation(list1, list2): 
    return sum([ abs(int(x)-int(y)) for x,y in zip(list1, list2)])

if __name__ == "__main__":
    dirs = os.listdir("train")
    for wavFile in dirs:
        rate, data = wav.read("train/" + wavFile)
        gender = wavFile.split('_')[1].split('.')[0]
        found = simpleRecognition(rate, data)
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
