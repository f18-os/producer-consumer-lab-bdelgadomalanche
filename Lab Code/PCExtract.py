#!/usr/bin/env python3

from PCQueue import *
import threading
import cv2
import numpy as np
import base64
import time

class extractFrames(threading.Thread):
    def __init__(self, fileName, outputBuffer):
        threading.Thread.__init__(self)
        self.fileName = fileName
        self.outputBuffer = outputBuffer
        
    def run(self):
        # Initialize frame count 
        count = 0
        
        # open video file
        vidcap = cv2.VideoCapture(self.fileName)

        # read first image
        success,image = vidcap.read()
        
        print("Reading frame {} {} ".format(count, success))
        while success:
            # get a jpg encoded frame
            success, jpgImage = cv2.imencode('.jpg', image)

            #encode the frame as base 64 to make debugging easier
            jpgAsText = base64.b64encode(jpgImage)

            #Wait for 50ms if queue is full
            while self.outputBuffer.full():
                time.sleep(.05)

            # add the frame to the buffer
            self.outputBuffer.put(jpgAsText)
        
            success,image = vidcap.read()
            print('Reading frame {} {}'.format(count, success))
            count += 1

        print("Frame extraction complete")
        #Finished production flag
        self.outputBuffer.put(None)
