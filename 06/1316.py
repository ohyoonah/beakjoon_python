# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 
# 각 문자가 연속해서 나타나는 경우

n = int(input())
group = 0

for i in range(n):
  string = input()
  error = 0

  for j in range(len(string)-1):
    if string[j] != string[j + 1]: #연달아 두 문자가 다를 때
      new_string = string[j + 1:] #현재 글자 이후 문자열을 새로운 단어로 생성
      if new_string.count(string[j]) > 0: #남은 문자열에서 현재 글자가 있다면
        error += 1
  
  if error == 0:
    group += 1 # error가 0이면 group단어로 체크

print(group)
