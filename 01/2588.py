# (세자리 수) * (세자리 수)

a = int(input())
b = int(input())

print(a * ((b % 100) % 10))
print(a * ((b % 100)//10))
print(a * (b // 100))
print(a * b)
