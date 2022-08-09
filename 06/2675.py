# 문자열 S를 입력받은 후에,
# 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램

t = int(input())

for i in range(t):
    r, s = input().split()

    for i in s:
        print(i * int(r), end='')
    # 줄 넘김
    print()
