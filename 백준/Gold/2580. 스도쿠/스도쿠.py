import sys
input = sys.stdin.readline

def chkRow(n, x):
    for i in range(9):
        if arr[x][i] == n:
            return False
    return True

def chkCol(n, y):
    for i in range(9):
        if arr[i][y] == n:
            return False
    return True

def chkSq(n, x, y):
    for i in range(3):
        for j in range(3):
            if arr[x//3 * 3 + i][y//3 * 3 + j] == n:
                return False
    return True

def dfs(cnt):
    if cnt == len(blank):
        for i in range(9):
            print(*arr[i])
        exit()
    x = blank[cnt][0]
    y = blank[cnt][1]
    for i in range(1, 10):
        if chkRow(i, x) and chkCol(i, y) and chkSq(i, x, y):
            arr[x][y] = i
            dfs(cnt+1)
            arr[x][y] = 0

arr = [list(map(int, input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))

dfs(0)