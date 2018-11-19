#!/usr/bin/env python3

import threading
import cv2
import numpy as np
import base64
import queue
import time

class convertFrames(threading.Thread):
    def __init__(self, lock, inputBuffer, outputBuffer):
        threading.Thread.__init__(self)
        self.lock = lock
        self.inputBuffer = inputBuffer
        self.outputBuffer = outputBuffer

    def run(self):
        # initialize frame count
        count = 0
        success = False
        
        while True:
            # get the next frame
            frameAsText = self.inputBuffer.get()

            if frameAsText == None:
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

            # add the frame to the buffer
            self.outputBuffer.put(jpgAsText)
            
            print('Converting frame {} {}'.format(count, success))
            count += 1
            
            #if queue is at 10 wait to add items
            self.lock.acquire()
            while self.outputBuffer.qsize() > 10:
                self.lock.release()
                time.sleep(.05)
                self.lock.acquire()
            self.lock.release()
            
