#!/usr/bin/env python3

import threading
from PCExtract import *
from PCConvert import *
from PCDisplay import *

# filename of clip to loadw
filename = 'clip.mp4'

lock = threading.Lock()

# shared queue  
extractionQueue = queue.Queue()
convertionQueue = queue.Queue()

extractionThread = extractFrames(lock,filename,extractionQueue)
conversionThread = convertFrames(lock,extractionQueue,convertionQueue)
displayThread = displayFrames(lock,convertionQueue)

conversionThread.start()
extractionThread.start()
displayThread.start()
