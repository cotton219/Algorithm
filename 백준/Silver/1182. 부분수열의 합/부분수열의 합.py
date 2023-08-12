import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for i in range(n)]
count = 0

def powerset(cnt):
    global count
    if (n == cnt):
        tot = 0
        for i in range(n):
            if visited[i]:
                tot += arr[i]
        if tot == s and True in visited:
            count += 1
        return
    visited[cnt] = True
    powerset(cnt+1)
    visited[cnt] = False
    powerset(cnt+1)

powerset(0)
print(count)