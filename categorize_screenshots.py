# Step 2

import os
import cv2 as cv
import shutil

screenshots = []

SCREENSHOTS_PATH = 'screenshots/'
POSITIVE_PATH = 'positive/'
NEGATIVE_PATH = 'negative/'

for filename in os.listdir(SCREENSHOTS_PATH):
    if os.path.isfile(os.path.join(SCREENSHOTS_PATH, filename)):
        screenshots.append(filename)

for screenshot_file in screenshots:
    file_path = os.path.join(SCREENSHOTS_PATH, screenshot_file)

    screenshot = cv.imread(file_path, cv.IMREAD_UNCHANGED)
    cv.imshow('Screenshot', screenshot)

    key = cv.waitKey() & 0xFF
    if key == ord('y'):
        print('Yes')
        shutil.move(file_path, os.path.join(POSITIVE_PATH, screenshot_file))
    else:
        print('No')
        shutil.move(file_path, os.path.join(NEGATIVE_PATH, screenshot_file))