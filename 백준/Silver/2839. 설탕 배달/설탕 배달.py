import sys
input = sys.stdin.readline

n = int(input())
pack = [5, 3]
m = 100001
for i in range(n//5+1):
    cnt = 100001
    nn = (n - i*5)
    if nn % 3 == 0:
        cnt = i + nn // 3
        nn = nn % 3

    m = min(cnt, m)
if m == 100001:
    print(-1)
else:
    print(m)