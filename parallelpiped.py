x, y, z = map(int,raw_input().split())
c = int(((y*z)/x)**0.5)
b = y/c
a = x/b
s = a+b+c
print 4*s
