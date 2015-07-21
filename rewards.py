import math
from math import *
a = map(int,raw_input().split())
b = map(int,raw_input().split())
n = int(raw_input())
a = sum(a)
b = sum(b)
c = ceil(a/5.0)
d = ceil(b/10.0)
if(n>=(c+d)):
	print "YES"
else:
	print "NO"

