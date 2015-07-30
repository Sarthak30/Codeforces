n, k = map(int, raw_input().split())
a = map(int,raw_input().split())
if(k>n):
	print "-1"
	exit()
else:
	a.sort(reverse = True)
	print a[k-1],0
