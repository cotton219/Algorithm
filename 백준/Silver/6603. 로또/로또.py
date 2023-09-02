import sys
input = sys.stdin.readline
from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        exit(0)

    for comb in combinations(arr[1:], 6):
        print(*comb)
    print()