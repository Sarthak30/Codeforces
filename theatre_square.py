from math import *

n,m,a = map(int,raw_input().split())
i= n/a
if(n%a!=0):
	i=i+1
j=m/a
if(m%a!=0):
	j=j+1
print str(i*j)

