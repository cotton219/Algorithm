def solution(id_list, report, k):
    id_dict = dict()

    for id in id_list:
        id_dict[id] = [[], 0]

    for rep in set(report):
        a, b = rep.split()
        # if b not in id_dict[a][0]:
        id_dict[a][0].append(b)
        id_dict[b][1] += 1

    result = []
    for i in id_dict:
        count = 0
        for j in id_dict[i][0]:
            if id_dict[j][1] >= k:
                count += 1
        result.append(count)

    return result