# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:17:28 2018

@author: tyagi
"""

class queue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        answer = self._data[self._front]
        self._front = (self._front + 1) % len (self._data)
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        if self._size == len(self._size):
            self._resize(2 * len(self._size))
        available = (self._front + self._size) % len(self._data)
        self._data[available] = e
        self._size += 1
        
    def _resize(self, c):
        old = self._data
        self._data = [None] * c
        w = self._front
        for k in range(self._size):
            self._data[k] = old[w]
            w = (1 + w) % len(old)
        self._front = 0