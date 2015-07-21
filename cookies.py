n = raw_input()
m = map(int,raw_input().split())
even = 0
odd = 0
for i in m:
	if(i%2==0):
		even = even+1
	else:
		odd = odd+1
s = sum(m)
if(s%2==0):
	print even
else:
	print odd
