import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def check(x, y, color):

    for i in range(4):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == color:
            cnt += 1
            if cnt == 5:
                if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and arr[x - dx[i]][y - dy[i]] == color:
                    break
                if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and arr[nx + dx[i]][ny + dy[i]] == color:
                    break
                print(color)
                print(x+1, y+1)
                sys.exit(0)

            nx += dx[i]
            ny += dy[i]


for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            check(i, j, arr[i][j])
print(0)