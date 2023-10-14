from collections import defaultdict

def solution(tickets): 
    answer = []
    visited = [False]*len(tickets)
    
    def dfs(start, result):
        
        if len(result) == len(tickets)+1:
            answer.append(result)
            return
        
        for idx, ticket in enumerate(tickets):
            if start == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], result + [ticket[1]])
                visited[idx] = False
        
    dfs('ICN', ["ICN"])
    
    answer.sort()
    return answer[0]
    