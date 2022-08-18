# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라
# 이들 소수의 합과 최솟값 찾는 프로그램

m = int(input())
n = int(input())
sosu_list = []

for i in range(m, n + 1):
  for j in range(2, i + 1):
    if j == i:
      sosu_list.append(i)
    if i % j == 0:
      break

if len(sosu_list) == 0:
  print(-1)
else:
  print(sum(sosu_list))
  print(min(sosu_list))