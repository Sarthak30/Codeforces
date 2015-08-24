x, n = map(int,raw_input().split())
k, m = map(int,raw_input().split())
a = map(int,raw_input().split())
b = map(int,raw_input().split())
if (a[k-1]<b[n-m]) :
	print "YES"
else:
	print "NO"
