sieve=[0]*2+[1]*1000001
for i in range(2,1001):
     if sieve[i]:
          for j in range(i*2,1000001,i):
               sieve[j]=0

n = input()
for i in map(int,raw_input().split()):
     print ['NO','YES'][int(i**0.5)*int(i**0.5) == i and sieve[int(i**0.5)]]
