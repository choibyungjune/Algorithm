n = int(input())

x = 1
y = 1

input_list = list(map(str, input().split()))

for direction in input_list:
    if direction == "L":
        if y - 1 <= 0:
            continue
        else:
            y -= 1
            
    elif direction == "R":
        if y + 1 > n:
            continue
        else:
            y += 1
    elif direction == "U":
        if x - 1 <= 0:
            continue
        else:
            x -= 1
    elif direction == "D":
        if x + 1 > n:
            continue
        else:
            x += 1
            
print(x, y)

# n = int(input())

# x = 1
# y = 1
# input_list = list(map(str, input().split()))
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# path = ['L', 'R', 'U', 'D']

# for direction in input_list:
#     for i in range(len(path)):
#         if direction == path[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#     if nx > 0 and ny > 0 and nx <= n and ny <=n: 
#         x, y = nx, ny
#     else:
#         continue

# print(x, y)