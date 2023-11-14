n, m = map(int, input().split())

large_in_smallest_num = -1e9
for i in range(n):
    input_list = list(map(int, input().split()))
    smallest = min(input_list)
    
    if large_in_smallest_num < smallest:
        large_in_smallest_num = smallest

print(large_in_smallest_num)

#O(n)