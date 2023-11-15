input_str = input()

y = input_str[0]
x = int(input_str[1])
translate_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,'e': 5, 'f': 6, 'g': 7, 'h': 8}
y = translate_dict[y]


cnt = 0
dx = [-1, 1, -2, 2, 2, -2, -1, 1]
dy = [2, 2, 1, 1, -1, -1, -2, -2]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        cnt += 1
    else:
        continue
    
print(cnt)

# input_str = input()

# y = ord(input_str[0]) - ord('a') + 1
# x = int(input_str[1])

# cnt = 0
# steps = [(-1, 2), (-1, -2), (-2, -1), (-2, 1), (1, 2), (1, -2), (2, -1), (2, 1)]


# for step in steps:
#     nx = x + step[0]
#     ny = y + step[1]
    
#     if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
#         cnt += 1
#     else:
#         continue
    
# print(cnt)