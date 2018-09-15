from pyAudioAnalysis import audioTrainTest as aT

aT.featureAndTrain(["data/1","data/2", "data/3", "data/4"], 
    1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)

print aT.fileClassification("data/test/zou3.wav", "svmSMtemp","svm")
