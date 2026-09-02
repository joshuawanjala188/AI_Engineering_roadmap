#it follows first in, first out

from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")


queue.popleft()

print(queue)