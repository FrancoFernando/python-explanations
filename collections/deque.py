'''
In Python 🐍 you can easily emulate stacks and queues using a deque.


A deque a list-like container with fast appends and pops at both ends.


These operations are thread-safe and much faster than when performed on a list.
'''

from collections import deque

def test_deque():
  d = deque([3,4,5]) # 3,4,5
  d.append(6) # 3,4,5,6
  d.appendleft(2) # 2,3,4,5,6
  d.pop() # 2,3,4,5
  d.popleft() # 3,4,5
