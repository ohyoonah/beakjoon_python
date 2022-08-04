# 현재 시간에 분 더하기

h, m = map(int, input().split())
t = int(input())
minute = t + m


if minute >= 60:
    if h+(minute//60) >= 24:
        print(h+(minute//60) - 24, minute % 60)
    else:
        print(h+(minute//60), minute % 60)
else:
    print(h, minute)
