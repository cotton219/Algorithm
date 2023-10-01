import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
dp1, dp2 = arr, arr

for _ in range(n-1):
    a, b, c = map(int, input().split())
    dp1 = [a + max(dp1[0], dp1[1]), b + max(dp1[0], dp1[1], dp1[2]), c + max(dp1[1], dp1[2])]
    dp2 = [a + min(dp2[0], dp2[1]), b + min(dp2[0], dp2[1], dp2[2]), c + min(dp2[1], dp2[2])]

mx = max(dp1)
mn = min(dp2)

print(mx, mn)