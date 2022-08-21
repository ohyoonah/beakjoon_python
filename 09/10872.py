# 0보다 크거나 같은 정수 N이 주어진다
# N!을 출력

def factorial(n):
  result = 1
  if n > 0:
    result = n * factorial(n - 1)
  return result

n = int(input())
print(factorial(n))


# 재귀함수 ==> 자기 자신을 호출하는 함수
