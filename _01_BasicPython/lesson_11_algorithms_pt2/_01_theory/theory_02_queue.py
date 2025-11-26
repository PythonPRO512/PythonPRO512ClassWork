from collections import deque

queue = deque()
print(queue)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

print(queue.popleft())
print(queue.popleft())
print(queue)
