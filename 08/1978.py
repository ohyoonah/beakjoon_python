# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력

n = int(input())
nums = list(map(int, input().split(' ')))
sosu = 0

for i in nums:
    cnt = 0 
    if i == 1:
        pass
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        sosu += 1

print(sosu)