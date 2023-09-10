import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, cnt):
    global result
    if cnt == k:
        if x == 0 and y == c-1:
            result += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != 'T' and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = False


r, c, k = map(int, input().split())
arr = [input().rstrip() for _ in range(r)]
visited = [[False] * c for _ in range(r)]

result = 0
visited[r-1][0] = True
dfs(r-1, 0, 1)
print(result)
