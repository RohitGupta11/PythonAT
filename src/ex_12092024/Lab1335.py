#dequeue double ended queue
#fifo=first in first out
#a list -like sequenece optimized for data access near its endpoints

from collections import  deque
#d=deque()
d= deque([1,2,3,4])
print(d)
d.append(5)
print(d)


#add element to the the left
d.appendleft(0)
print(d)


#extend  to the the right
d.extend([17,8])
print(d)
print(d.pop()) # remove from left
print(d)
print(d.popleft()) # remove from right
print(d)