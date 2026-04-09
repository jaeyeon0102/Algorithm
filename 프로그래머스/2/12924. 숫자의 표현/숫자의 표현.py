def solution(n):
    answer = 1
    list = []
    
    
    if n == 1 or n == 2:
        return answer
    else:
        for i in range(n//2 +2):
            list.append(i)
            if sum(list) > n:
                while sum(list) > n:
                    list.pop(0)
            if sum(list) == n:
                answer += 1
    return answer