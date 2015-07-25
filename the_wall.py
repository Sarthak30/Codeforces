x, y, a, b = map(int,raw_input().split())


def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


l = lcm(x, y)
lower = a/l
higher = b/l
if( l*lower<a):
	lower = lower + 1

print higher-lower+1
