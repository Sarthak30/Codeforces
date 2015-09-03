n,m = map(int,raw_input().split())
if n == 1:
    print 1
else:
    print m+1 if n-m > m-1 else m-1
