from fractions import gcd
y, w = map(int,raw_input().split())
d = 6-max(y,w)+1
f = gcd(d,6)
d = d/f
a = 6/f
print str(d)+"/"+str(a)
