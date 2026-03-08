'''
dictionary -> A : 값
알파벳마다 자릿수에 따른 값을 저장한다 (ex. AB = [A : 10] [B : 1])
딕셔너리에 들어있는 알파벳의 값들을 정렬하여 9부터 순차적으로 값을 곱해서 전체를 더함
'''

alpha_dict = {}

n = int(input())

for i in range(n):
    s = str(input())

    for j in range(len(s)):
        if s[j] in alpha_dict:
            alpha_dict[s[j]] += 10**(len(s) -j-1)
        else:
            alpha_dict[s[j]] = 10**(len(s) -j-1)

sorted_dict = sorted(alpha_dict.items(),key = lambda x : x[1],reverse=True)

num = 9
ans = 0
for i in range(len(sorted_dict)):
    ans += num *sorted_dict[i][1]
    num -= 1
print(ans)
    