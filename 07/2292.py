# 벌집
n = int(input())
count = 1
result = 1 # 벌집 개수

# 1 -> 6 -> 12 -> 18 -> 24 -> .. +6

while n > result:
  result += 6 * count 
  count += 1

print(count)