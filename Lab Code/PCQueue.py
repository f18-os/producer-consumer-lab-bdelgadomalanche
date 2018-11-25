#!/usr/bin/env python3

#Queue implementation provided by Dr. Freudenthal
#Modified to lock the queue when being accesesed
#and to be able to check the size of the queue
#to see when it's empty or full
class PCQueue:
    def __init__(self, size, lock):
        self.consumables = []
        self.lock = lock
        self.size = size
        self.length = 0
        
    def put(self, item):
        with self.lock:
            self.consumables.append(item)
            self.length += 1
    
    def get(self):
        with self.lock:
            consumables = self.consumables
            item = consumables[0]
            del consumables[0]
            self.length -= 1
            return item
    
    def empty(self):
        if self.length == 0:
            return True
        return False
    
    def full(self):
        if self.length == self.size:
            return True
        return False
    
    def __repr__(self):
        return "Q(%s)" % self.consumables
