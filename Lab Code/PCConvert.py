#!/usr/bin/env python3

from PCQueue import *
import threading
import cv2
import numpy as np
import base64
import time

class convertFrames(threading.Thread):
    def __init__(self, inputBuffer, outputBuffer):
        threading.Thread.__init__(self)
        self.inputBuffer = inputBuffer
        self.outputBuffer = outputBuffer

    def run(self):
        # initialize frame count
        count = 0
        success = False
        
        while True:
            if not self.inputBuffer.empty():
                # get the next frame
                frameAsText = self.inputBuffer.get()

                if frameAsText == None:
                    #Finished production flag
                    self.outputBuffer.put(None)
                    break
                
                # decode the frame 
                jpgRawImage = base64.b64decode(frameAsText)

                # convert the raw frame to a numpy array
                jpgImage = np.asarray(bytearray(jpgRawImage), dtype=np.uint8)
                
                # get a jpg encoded frame
                img = cv2.imdecode( jpgImage ,cv2.IMREAD_UNCHANGED)
                
                # convert the image to grayscale
                grayscaleFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
                # get a jpg encoded frame
                success, jpgConvImage = cv2.imencode('.jpg', grayscaleFrame)
                
                #encode the frame as base 64 to make debugging easier
                jpgAsText = base64.b64encode(jpgConvImage)

                #Wait for 50ms if queue is full
                while self.outputBuffer.full():
                    time.sleep(.05)

                # add the frame to the buffer
                self.outputBuffer.put(jpgAsText)
                
                print('Converting frame {} {}'.format(count, success))
                count += 1
