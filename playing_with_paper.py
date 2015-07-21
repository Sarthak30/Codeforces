a, b = map(int,raw_input().split())
count = 0
while (a>0 and b>0):
	if(a<b):
		count = count + int(b/a)
		b = b%a
	else:
		count = count + int(a/b)
		a = a%b
print count
