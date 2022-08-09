# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

s = input().upper()
set_s = list(set(s))

s_list = []

for i in set_s:
    count = s.count(i)
    s_list.append(count)

if s_list.count(max(s_list)) > 1:
    print('?')
else:
    max_index = s_list.index(max(s_list))
    print(set_s[max_index])
