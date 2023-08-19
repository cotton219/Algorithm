import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
edges = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [0] * (n+1)

def dfs(start):
    for i in edges[start]:
        if visited[i] == 0:
            visited[i] = start
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])