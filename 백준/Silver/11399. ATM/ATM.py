n = int(input())
waiting_people = list(map(int, input().split())) 

# i 번째 사람이 돈을 인출하는데 필요한 시간
# 누적 시간
# 누적 리스트 만들기
waiting_people.sort()

for i in range(1, len(waiting_people)):
    waiting_people[i] += waiting_people[i - 1]

print(sum(waiting_people))