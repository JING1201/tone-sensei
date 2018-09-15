from pyAudioAnalysis import audioTrainTest as aT
import classifier

# aT.shortTermWindow=0.05
# aT.shortTermStep = 0.05

#aT.featureAndTrain(["data/1","data/2", "data/3", "data/4"], 
#    0.5, 0.5, 0.03, 0.03, "svm", "toneClassifier", False)

PATH_TO_WAV = "data/test/ma2.wav"
PATH_TO_CLASSIFIER = "toneClassifier"
print aT.fileClassification(PATH_TO_WAV, PATH_TO_CLASSIFIER,"svm")
print classifier.classify(PATH_TO_WAV, PATH_TO_CLASSIFIER)
