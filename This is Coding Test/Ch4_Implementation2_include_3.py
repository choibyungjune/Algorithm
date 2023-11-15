import time
#my answer
n = int(input())

start_time = time.time()
# 3 in min/sec
three = 15*60 + 45*15
total = 0
for i in range(n + 1):
    if i == 3 or i == 13 or i == 23:
        total += 3600
    else:
        total += three

end_time = time.time()

print(total)
print(end_time - start_time)

#O(1)
# n = int(input())
# start_time = time.time()

# cnt = 0
#  for i in range(n + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 cnt += 1
# end_time = time.time()

# print(cnt)
# print(end_time - start_time)