# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 
# 예를 들어, 734와 893을 칠판에 적었다면, 
# 상수는 이 수를 437과 398로 읽는다.
# 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

num1, num2 = input().split()

num1_reverse = int(num1[::-1])
num2_reverse = int(num2[::-1])

print(max(num1_reverse, num2_reverse))