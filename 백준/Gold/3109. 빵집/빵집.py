import sys
sys.stdin.readline

dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(x, y):
    if y == c-1:
        return True

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if graph[nx][ny] != "x" and visited[nx][ny] == False:
            visited[nx][ny] = True
            if dfs(nx, ny):
                return True
    return False


r, c = map(int,input().split())
visited = [[False] * c for _ in range(r)]
graph = [list(input().strip()) for _ in range(r)]

cnt = 0
for i in range(r):
    if dfs(i, 0):
        cnt += 1

print(cnt)
