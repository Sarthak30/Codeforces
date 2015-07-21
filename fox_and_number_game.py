n = int(raw_input())
m = map(int,raw_input().split())
m = sorted(m, reverse=True)

def GCD(a, b):

    if b == 0:
        return a
    else:
        return GCD(b, a % b)
        
gcd = reduce(lambda x,y:GCD(x,y),m)

print gcd*n
