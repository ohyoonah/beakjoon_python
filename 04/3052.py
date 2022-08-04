# 10개의 자연수를 42로 나눈 나머지의 서로 다른 값의 개수

array = []

for i in range(10):
    n = int(input())
    array.append(n % 42)

result = set(array)
print(len(result))


# 파이썬에서 set()은 중복되는 수를 제거해 준다
# set을 사용해 중복되는 수를 제거한 다음, len으로 남은 값의 길이를 출력한다.
