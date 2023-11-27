'''
문제 풀이 아이디어:
연속된 1 , 0의 개수 중 min 값 반환 
'''

S = input()

lst = [int(i) for i in S]

zero_cnt = 0
one_cnt = 0

if lst[0] == 0:
    zero_cnt += 1
elif lst[0] == 1:
    one_cnt += 1
    
for i in range(1, len(lst)):
    if lst[i] != lst[i - 1]:
        if lst[i] == 0:
            zero_cnt += 1
        elif lst[i] == 1:
            one_cnt += 1
    else:
        continue
    
# print(zero_cnt)
# print(one_cnt)
print(min(zero_cnt,one_cnt))