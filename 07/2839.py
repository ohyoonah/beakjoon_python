# 봉지는 3킬로그램 봉지와 5킬로그램 봉지

n = int(input())
result = 0

while n >= 0:
  # 5로 나눴을 때 나머지가 없을 경우 나눈 몫을 담아줌
  if n % 5 == 0:
    result += (n // 5)
    print(result)
    break
  
  n -= 3
  result += 1

else:
  print(-1)