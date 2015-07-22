import math
from math import factorial

def combination(n,r):
    return float(factorial(n)) / float(factorial(r)) / float(factorial(n-r))

a = raw_input()
ap = a.count('+')
am = a.count('-')
b = raw_input()
bp = b.count('+')
bm = b.count('-')
n = b.count('?')
x = float(ap-bp)
y = float(am-bm)
if(x<0 or y<0 or x+y!=n):
    print(0.0)
else:
    print(combination(n,x)/(1<<n))
