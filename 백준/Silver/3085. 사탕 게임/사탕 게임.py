import sys
Input = sys.stdin.readline

def count_box(box):
    Max_result = 1

    for i in range(a):

        #열 순회
        count = 1
        for j in range(1,a):
            if(box[i][j] == box[i][j-1]): # 왼쪽, 오른쪽 비교
                count += 1 # 이전 것과 같다면 cnt에 1 더하기
            else:
                count = 1 # 이전과 다르다면 다시 1로 초기화

            if(count > Max_result ):
                Max_result = count

        count = 1        
        for j in range(1, a):
            if(box[j][i] == box[j-1][i]): # 위아래 비교
                count += 1
            else:
                count = 1
            if(count > Max_result ):
                Max_result = count

    return Max_result

a = int(Input())
box = [list(Input()) for _ in range(a) ]
answer = 0

for i in range(a):
    for j in range(a):
        #열 바꾸기(가로)
        if(j+1 < a):
            #인접한것 바꾸기, 같은것도 바꾼다.
            box[i][j], box[i][j+1] =box[i][j+1], box[i][j]
            temp = count_box(box)

            answer = max(temp, answer)

            #다시 돌려놓기
            box[i][j], box[i][j+1] =box[i][j+1], box[i][j]

        #행바꾸기(세로)
        if(i+1 < a):
            #인접한것 바꾸기, 같은것도 바꾼다.
            box[i][j], box[i+1][j] =box[i+1][j], box[i][j]
            temp = count_box(box)
            answer = max(temp, answer)

            #다시 돌려놓기
            box[i][j], box[i+1][j] =box[i+1][j], box[i][j]

print(answer)