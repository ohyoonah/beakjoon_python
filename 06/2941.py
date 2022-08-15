# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# 위 목록에 없는 알파벳은 한 글자씩 센다.

string = input()
array = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# string_list = []

# for i in array:
#   if i in string:
#     string_list.append(i)

# for j in range(len(string_list)):
#   string = string.replace(string_list[j], "")

# print(len(string_list + (list(string))))

for i in array:
  string = string.replace(i, '.')
print(len(string))


# replace는 문자열을 변경하는 함수
# 변수.replace(old, new, [count])
# old: 현재 문자열에서 변경하고 싶은 문자
# new: 새로 바꿀 문자
# count: 변경할 횟수
# array에 포함된 문자열은 .으로 변경한 다음 문자열의 길이를 구함

# 위 주석처럼 풀면 string안에서 array문자가 겹칠 시 카운트가 제대로 안 됨