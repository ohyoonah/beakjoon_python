# 주사위 굴리기
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

n1, n2, n3 = map(int, input().split())

money = 0

if n1 == n2 and n2 == n3:
    money = 10000+n1*1000
elif n1 != n2 and n2 != n3 and n1 != n3:
    money = max(n1, n2, n3)*100
else:
    if (n1 == n2 and n1 != n3) or (n1 == n3 and n1 != n2):
        money = 1000 + n1 * 100
    elif n2 == n3 and n1 != n2:
        money = 1000 + n3 * 100

print(money)
