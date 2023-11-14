n, m, k = map(int, input().split())
input_list = list(map(int, input().split()))

input_list.sort()
largest_num = input_list.pop()
second_largest_num = input_list.pop()
total = 0
for i in range(m):
    if i != 0 and i % k == 0:
        total += second_largest_num
    else:
        total += largest_num
        
print(total)


#O(n)