from itertools import permutations

# 가능한 숫자 조합 생성
nums = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

t = int(input())

# 가능한 숫자 조합 개수 초기화
count = 0

for i in range(t):
    n, s, b = map(int, input().split())
    n = list(str(n))

    # 조건에 맞는 숫자 조합 개수 카운트
    for num in nums[:]:
        strike, ball = 0, 0
        for j in range(3):
            if num[j] == n[j]:
                strike += 1
            elif n[j] in num:
                ball += 1
        if strike != s or ball != b:
            nums.remove(num)


print(len(nums))