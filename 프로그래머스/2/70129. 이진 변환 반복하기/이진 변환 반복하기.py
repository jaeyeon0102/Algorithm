def solution(s):
    answer = [0,0]
    
    while s != '1':
        cnt = s.count('1')
        answer[1] += len(s) - cnt
        s = str(bin(int(cnt_1))[2:])
        answer[0] += 1
    return answer

def solution(s):
    answer = [0, 0]

    while s != '1':
        s_removed_0 = ""
        cnt_1 = s.count('1')
        answer[1] += len(s) - cnt_1
        s = str(bin(int(cnt_1))[2:])
        answer[0] += 1

    return answer