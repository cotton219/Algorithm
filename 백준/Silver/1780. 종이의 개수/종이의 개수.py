import sys
input = sys.stdin.readline

def sol(x, y, n):
    value = arr[x][y]
    same = True
    for a in range(x, x + n):
        for b in range(y, y + n):
            if arr[a][b] != value:
                same = False
                break
        if not same:
            break

    if same:
        result_dict[value] += 1
        return

    for i in range(3):
        for j in range(3):
            sol(x + i * n//3, y + j * n//3, n//3)

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
result_dict = {-1:0, 0:0, 1:0}
sol(0, 0, n)

print(result_dict[-1])
print(result_dict[0])
print(result_dict[1])

