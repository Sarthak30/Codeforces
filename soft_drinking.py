n, k, l, c, d, p, nl, np = map(int,raw_input().split())
a = k*l
x = a/nl
y = c*d
z = p/np
print min(x,y,z)/n
