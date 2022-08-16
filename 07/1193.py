n = int(input())

# 1/1 ==  2
# 1/2 -> 2/1 ==  3
# 3/1 -> 2/2 -> 1/3 == 4
# .. 합이 1씩 늘어남

# 합이 2 => 1개
# 합이 3 => 2개

line = 1

while n > line:
  n -= line
  line += 1

if line % 2 == 0:
  a = n
  b = line - n + 1
else:
  a = line - n + 1
  b = n

print(f'{a}/{b}')