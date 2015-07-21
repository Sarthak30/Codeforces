a, b = map(int,raw_input().split())
f = 0
d = 0
s = 0
for i in range(1,7):
	if(abs(i-a)<abs(i-b)):
		f = f+1
	elif(abs(i-a)==abs(i-b)):
		d = d+1
	else:
		s = s+1
print f,
print d,
print s,
