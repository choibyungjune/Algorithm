'''
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다

해결 전략
- 뒤에 연속적으로 나온 + 는 다 묶는다 -> 다음 - 가 나올 때까지
- 가 나오면 무조건 나머지는 다 음수가 나와야한다.

'''

from re import split
sign = []

problem = input()

#1. 입력 받기
for i in range(len(problem)):
    if problem[i] == '-':
        sign.append('-')
    elif problem[i] == '+':
        sign.append('+')
        
numbers = split(r'[\-\+]', problem)
numbers = [int(i) for i in numbers]


total = numbers[0]

is_minus = False
for i in range(len(sign)):
    if is_minus == False:
        if sign[i] == '+':
            total += numbers[i + 1]
        else:
            is_minus = True
            total -= numbers[i + 1]
    else:
        total -= numbers[i + 1]
print(total)

