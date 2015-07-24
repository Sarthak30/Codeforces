(n, m) = map(int,raw_input().split())
def f(a, b):
    if (b <= a):
        return a - b
    return 1 + b % 2 + f(a, (b + 1) / 2)
print f(n, m)
