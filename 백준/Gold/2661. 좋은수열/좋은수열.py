import sys
input = sys.stdin.readline

def product(cnt):
    for i in range(1, (cnt//2) + 1):
        if nums[-i:] == nums[-2 * i:-i]:
            return -1

    if cnt == n:
        print(*nums, sep='')
        return 0

    for i in range(1, 4):
        nums.append(i)
        if product(cnt + 1) == 0:
            return 0
        nums.pop()

n = int(input())
nums = []
product(0)