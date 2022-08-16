# 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램

# test data
t = int(input())

for i in range(t):
  #호텔 층 수, 각 층 방 수, 몇 번째 손님인지
  h, w, n = map(int, input().split())
  num = (n // h) + 1
  floor = n % h
  if n % h == 0:
    num = n // h
    floor = h
  print(f'{floor * 100 + num}')