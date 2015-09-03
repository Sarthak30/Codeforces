n, w = map(int,raw_input().split())
a = sorted(map(int,raw_input().split()))
print min(w,3*a[0]*n,a[n]*1.5*n)
