# ex) "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점

n = int(input())
for i in range(n):
    score = input()
    count = 0
    sum_count = 0

    for j in score:
        if j == 'O':
            count += 1
            sum_count += count
        else:
            count = 0

print(sum_count)
