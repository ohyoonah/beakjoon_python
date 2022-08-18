# 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다
# n보다 크고, 2n보다 작거나 같은 소수의 개수

# 테스트 케이스 총 범위
n=123456

def prime_list(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True		

primes_list = list(range(2,246912))
ans_list = []

for i in primes_list:
    # 만약 소수에 해당하면 prime_list 함수에서 true를 반환 받을 것
    if prime_list(i):
        # true를 반환 받는다면 ans_list에 해당 원소(i)를 추가
        ans_list.append(i)
        
        
while True:
    
    cnt = 0

    num = int(input())

    # 0을 입력받으면 종료    
    if num == 0:
        break
    
    for i in ans_list:
        if num < i < 2*num+1:
            cnt += 1
            
    print(cnt)