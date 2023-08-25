# Step 3

import os

NEGATIVE_PATH = 'negative/'

with open('neg.txt', 'w') as f:
    for file_name in os.listdir(NEGATIVE_PATH):
        f.write(NEGATIVE_PATH + file_name + '\n')

# For generating the positive text file:
# C:\Users\CriShoux\Downloads\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images=positive/

# For creating samples:
# C:\Users\CriShoux\Downloads\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec

# For training:
# Also note: https://answers.opencv.org/question/84852/traincascades-error-required-leaf-false-alarm-rate-achieved-branch-training-terminated/
# C:\Users\CriShoux\Downloads\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 165 -numNeg 1000 -numStages 7 -minHitRate 0.999 -maxFalseAlarmRate 0.19