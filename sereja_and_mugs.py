n, s = map(int,raw_input().split())
a = map(int, raw_input().split())
s1 = sum(a)
m = max(a)
s1 = s1-m
if(s1<=s):
	print "YES"
else:
	print "NO"
