'''
File that contains the function for the classifier to classify a given wav file
Implemented for server use
'''

from pyAudioAnalysis import audioTrainTest as aT

def classify(PATH_TO_WAV, PATH_TO_CLASSIFIER):
    results = aT.fileClassification(PATH_TO_WAV, PATH_TO_CLASSIFIER,"svm")
    results = list(results[1]) #extract the matrix
    return results.index(max(results))+1
