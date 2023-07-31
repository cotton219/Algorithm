import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    dx1 = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy1 = [0, -1, -1, -1, 0, 1, 1, 1]

    dx2 = dx1[::-1]
    dy2 = dy1[::-1]

    x = n//2
    y = n//2

    angle = abs(d//45)
    for k in range(angle):
        for j in range(1, x+1):
            if d > 0:
                for i in range(7):
                    temp = graph[x + dx1[i]*j][y + dy1[i]*j]
                    graph[x + dx1[i]*j][y + dy1[i]*j] = graph[x + dx1[i+1]*j][y + dy1[i+1]*j]
                    graph[x + dx1[i+1]*j][y + dy1[i+1]*j] = temp
            else:
                for i in range(7):
                    temp = graph[x + dx2[i]*j][y + dy2[i]*j]
                    graph[x + dx2[i]*j][y + dy2[i]*j] = graph[x + dx2[i+1]*j][y + dy2[i+1]*j]
                    graph[x + dx2[i+1]*j][y + dy2[i+1]*j] = temp

    for i in range(n):
        print(*graph[i])
