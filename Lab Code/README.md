# Overview:
This lab uses Dr. Freudenthal's code to implement Producer Consumer behavior
using threads.

# Steps:
Simply run PCLab.py

## File List
### ExtractFrames.py
Extracts a series of frames from the video contained in 'clip.mp4' and saves 
them stores them in a buffer.

### ConvertToGrayscale.py
Loads a series of frames from a buffer, converts the grames to grayscale, 
and sends them to an output buffer.

### PCDisplay.py
Loads a series of frames sequently from a buffer and displays them with a 42ms delay.

### PCQueue.py
Custom queue class that takes a lock and a size to handle production storage.

### PCLab.py
Runs previous classes as threads and sends shared input and output buffer queues for 
Producer Consumer logic.

# Resources:
Used the source code provided to us

# Collaborators:
Found on COLLABOTATORS.md file
