# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지

array = []

for i in range(9):
    array.append(int(input()))
print(max(array))
print(array.index(max(array)) + 1)
