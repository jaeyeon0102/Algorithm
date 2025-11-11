# 계산 함수
def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

# 괄호 추가 함수
def dfs(idx, current):
    global max_result

    # 만약 연산자가 범위 밖이라면
    if idx >= N:
        # 최댓값 갱신 후 리턴
        max_result = max(max_result,current)
        return
    
    # 연산자
    op = numlist[idx]
    # 다음 숫자
    next_num = int(numlist[idx+1])

    # 괄호가 없는 경우에 대해 다음 연산자와 연산 진행
    dfs(idx +2, calc(current,op,next_num))

    # 만약 idx +2가 범위 내에 있다면
    if idx + 2 < N:

        # 다음 연산자
        op2 = numlist[idx +2]
        # 다다음 연산에 대한 값을 미리 계산 (괄호)
        second_num = int(numlist[idx+3])
        bracket = calc(next_num, op2, second_num)
        # dfs 수행
        dfs(idx+4, calc(current,op, bracket))


# 입력
N = int(input())

max_result = -float('inf')
numlist = list(map(str, input().strip()))

# dfs(연산자, 숫자)
dfs(1, int(numlist[0]))
print(max_result)