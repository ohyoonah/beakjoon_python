# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력

import sys
c = int(input())

for i in range(c):
    a = list(map(int, sys.stdin.readline().split()))
    count = 0
    avg = sum(a[1:]) / int(a[0])

    for j in a[1:]:
        if avg < j:
            count += 1
    result = (count / int(a[0]) * 100)
    print(f'{result:.3f}%')

# {result:.3f}를 사용해서 소수점을 셋째자리까지 만들어 줌
# 40.0으로 결과가 나와도 40.000이 될 수 있게
