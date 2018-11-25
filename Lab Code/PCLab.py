#!/usr/bin/env python3

import threading
import PCQueue
from PCExtract import *
from PCConvert import *
from PCDisplay import *

# filename of clip to loadw
filename = 'clip.mp4'

lock = threading.Lock()

# shared queues
extractionQueue = PCQueue(10, lock)
convertionQueue = PCQueue(10, lock)

extractionThread = extractFrames(filename,extractionQueue)
conversionThread = convertFrames(extractionQueue,convertionQueue)
displayThread = displayFrames(convertionQueue)

conversionThread.start()
extractionThread.start()
displayThread.start()
