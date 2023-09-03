import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 1
visited = [[False]*m for _ in range(n)]
visited[r][c] = True

while True:
    clean = 0
    for _ in range(4):
        d = (d+3)%4
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                cnt += 1
                r = nx
                c = ny
                clean = 1
                break

    if clean == 0:
        if arr[r - dx[d]][c - dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dx[d], c - dy[d]

