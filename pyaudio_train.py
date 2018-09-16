from pyAudioAnalysis import audioTrainTest as aT
import classifier
import os
import re

# aT.shortTermWindow=0.05
# aT.shortTermStep = 0.05

aT.featureAndTrain(["data/1","data/2", "data/3", "data/4"], 
    0.5, 0.5, 0.03, 0.03 , "svm", "toneClassifier", False)

PATH_TO_WAV = "data/test/hou4.wav"
PATH_TO_CLASSIFIER = "toneClassifier"
print aT.fileClassification(PATH_TO_WAV, PATH_TO_CLASSIFIER,"svm")
print classifier.classify(PATH_TO_WAV, PATH_TO_CLASSIFIER)

directory = 'data/test'
corrects = 0
total = 0
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        detected_tone = classifier.classify(directory+'/'+filename, PATH_TO_CLASSIFIER)
        actual_tone = re.search(r'\d+', filename).group()
        #rint "Detected tone is "+str(detected_tone)+" and actual tone is "+str(actual_tone)
        if detected_tone == int(actual_tone):
            corrects += 1
        total += 1

if total!=0:
    accuracy = corrects/(total+0.0)
    print "Accuracy: "+str(accuracy)

