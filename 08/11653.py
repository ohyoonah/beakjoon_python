# 정수 N이 주어졌을 때, 소인수분해

n = int(input())
d = 2

if n == 1:
  pass

while n > 1:
  if n % d == 0:
    print(d)
    n = n / d
  else:
    d = d + 1
