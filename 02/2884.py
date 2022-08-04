# 45분 일찍 일어나기

h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
else:
    if h == 0:
        print(23, (m-45)+60)
    else:
        print(h-1, (m-45)+60)
