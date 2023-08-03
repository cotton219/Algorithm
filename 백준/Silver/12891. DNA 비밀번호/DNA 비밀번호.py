import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input().rstrip()
a, c, g, t = map(int, input().split())

dict_part = {'A': 0,'C': 0,'G': 0,'T': 0}
start, end = 0, p-1

cnt = 0

word = dna[start:end]

for w in word:
    dict_part[w] += 1

while end < s:
    # for w in word:
    #     dict_part[w] += 1
    dict_part[dna[end]] += 1
    if dict_part['A'] >= a and dict_part['C'] >= c and dict_part['G'] >= g and dict_part['T'] >= t:
        cnt += 1
    dict_part[dna[start]] -= 1
    start += 1
    end += 1


print(cnt)


