import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

queue = deque([i for i in range(1, n+1)])

result = 0
while targets:
    target = targets.pop(0)
    if queue[0] == target:
        queue.popleft();
    else:
        idx = queue.index(target)
        l = len(queue)
        if idx <= l//2:
            result += idx
            for i in range(idx):
                queue.rotate(-1)
        else:
            result += (l - idx)
            for i in range(l-idx):
                queue.rotate(1)
        queue.popleft()
print(result)