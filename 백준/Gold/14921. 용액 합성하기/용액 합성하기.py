'''
용액 합성하기 14921번

문제
-100,000,000 <= 용액 <= 100,000,000

0에 가장 가까운 용액 만들기

용액들의 특성값이 오름차순으로 주어짐

-101, -3, -1, 5, 93


- 모두가 양수일 때!!
'''

N = int(input())

solution = list(map(int,input().split()))

result = 200000001

left = 0
right = N - 1

while left < right:
    s = solution[left] + solution[right]

    if abs(s) < abs(result):
        result = s
    
    if s > 0:
        right -= 1
    else:
        left += 1



print(result)