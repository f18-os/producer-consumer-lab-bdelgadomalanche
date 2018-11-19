#!/usr/bin/env python3

import threading
import cv2
import numpy as np
import base64
import queue
import time

class extractFrames(threading.Thread):
    def __init__(self, lock, fileName, outputBuffer):
        threading.Thread.__init__(self)
        self.lock = lock
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

            # add the frame to the buffer
            self.outputBuffer.put(jpgAsText)
        
            success,image = vidcap.read()
            print('Reading frame {} {}'.format(count, success))
            count += 1
            
            #if queue is at 10 wait to add items
            self.lock.acquire()
            while self.outputBuffer.qsize() > 10:
                self.lock.release()
                time.sleep(.05)
                self.lock.acquire()
            self.lock.release()

        print("Frame extraction complete")
        self.outputBuffer.put(None)
