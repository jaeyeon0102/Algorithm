'''
한 보트에 최대 2명
무게 제한 

무게 제한 // 2 이상인 애들은 다 1명씩만 가능함
그 이하인 애들만 계산.
'''
def solution(people, limit):
    answer = 0
    people.sort()
    
    i,j = 0, len(people)-1
    
    while i <= j:
        if people[i] + people[j] <= limit:
            answer += 1
            i += 1
            j -= 1
        else:
            answer += 1
            j -= 1
    
    return answer