# Step 1

import mss
import time

sct = mss.mss()

SCREENSHOTS_PATH = 'screenshots/'

while True:
    screenshot = sct.grab((0, 0, 1920, 1080))

    png = mss.tools.to_png(screenshot.rgb, screenshot.size)

    epoch_time = time.time()

    with open(SCREENSHOTS_PATH + str(epoch_time) + '.png', 'wb') as f: 
        f.write(png)

    time.sleep(0.4)