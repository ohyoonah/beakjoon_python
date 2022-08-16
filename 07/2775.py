# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# 아파트에는 0층부터 있고 각층에는 1호부터 있으며
# 0층의 i호에는 i명이 산다.

t = int(input())

for i in range(t):
  #층
  k = int(input())
  #호
  n = int(input())
  # 0층
  floor_0 = [j for j in range(1, n + 1)]

  for x in range(k):
    for y in range(1, n):
      floor_0[y] += floor_0[y - 1]
  print(floor_0[-1])

