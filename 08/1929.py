# M이상 N이하의 소수를 모두 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력

m, n = map(int, input().split())

def isprime(m, n):
  n += 1                            
  prime = [True] * n                
  for i in range(2, int(n**0.5)+1): 
    if prime[i]:                    
      for j in range(2*i, n, i):    
        prime[j] = False

  for i in range(m, n):
    if i > 1 and prime[i] == True:  
      print(i)

isprime(m, n)