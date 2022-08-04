# 점수 수정
# 최고점 = M
# 점수 / M * 100으로 수정한 후 평균 구하기

# 1차 코드!! 결과 --> 런타임에러
#n = int(input())
# for i in range(n):
#    score = list(map(int, input().split()))
#    m = max(score)
#    print((sum(score)/m * 100) / len(score))

# 2차 수정 코드
n = int(input())
score = list(map(int, input().split()))
m = max(score)
array = []

for i in score:
    array.append(i/m*100)

print(sum(array) / n)
