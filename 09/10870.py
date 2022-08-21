# 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1
# 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합
# Fn = Fn-1 + Fn-2 (n ≥ 2)

def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)  

n = int(input())
print(fibonacci(n))