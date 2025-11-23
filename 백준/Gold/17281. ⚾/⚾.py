'''
선수들 순서 배정 (4번타자 지정되어있음)
-> 2~9번 선수들 permutation 으로 순서 배정

permutation 별로 for문 -> 순서대로 타자 결과 저장 -> 아웃 3번이면 이닝 종료
아웃카운트 세기
마지막 타자 기억
'''
import sys
input = sys.stdin.readline

from itertools import permutations

N = int(input())

results = [list(map(int,input().split())) for _ in range(N)]

max_score = 0

# 지명 타자인 1번 타자 제외 
players = [i for i in range(2, 10)]


for order in permutations(players):
    # 4번자리에 1번 지명
    lineup = [x-1 for x in (list(order[:3]) + [1] + list(order[3:]))]

    score = 0
    hitter = 0

    # 이닝마다
    for inning in range(N):
        outs = 0
        bases = [0,0,0] # 1~3루

        while outs <3:
            result = results[inning][lineup[hitter]]

            if result == 0:
                outs += 1

            elif result == 1: # 1루타
                if bases[2]: score += 1
                bases[2] = bases[1]
                bases[1] = bases[0]
                bases[0] = 1

            elif result == 2: # 2루타
                if bases[2]: score += 1
                if bases[1]: score += 1
                bases[2] = bases[0]
                bases[1] = 1
                bases[0] = 0

            elif result == 3: # 3루타
                score += bases[2] + bases[1] + bases[0]
                bases = [0, 0, 1]

            else:
                score += bases[0] + bases[1] + bases[2] + 1
                bases = [0, 0, 0]


            hitter = (hitter + 1) % 9

    max_score = max(max_score, score)
print(max_score)