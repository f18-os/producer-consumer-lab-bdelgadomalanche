#!/usr/bin/env python3

from PCQueue import *
import threading
import cv2
import numpy as np
import base64
import time

class displayFrames(threading.Thread):
    def __init__(self, inputBuffer):
        threading.Thread.__init__(self)
        self.inputBuffer = inputBuffer

    def run(self):
        # initialize frame count
        count = 0

        # go through each frame in the buffer until the buffer is empty
        while True:
            if not self.inputBuffer.empty():
                # get the next frame
                frameAsText = self.inputBuffer.get()

                if frameAsText == None:
                        break

                # decode the frame 
                jpgRawImage = base64.b64decode(frameAsText)

                # convert the raw frame to a numpy array
                jpgImage = np.asarray(bytearray(jpgRawImage), dtype=np.uint8)
                
                # get a jpg encoded frame
                img = cv2.imdecode( jpgImage ,cv2.IMREAD_UNCHANGED)

                print("Displaying frame {}".format(count))        

                # display the image in a window called "video" and wait 42ms
                # before displaying the next frame
                cv2.imshow("Video", img)
                if cv2.waitKey(42) and 0xFF == ord("q"):
                    break
                count += 1

        print("Finished displaying all frames")
        # cleanup the windows
        cv2.destroyAllWindows() 
