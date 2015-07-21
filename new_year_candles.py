a,b = map(int,raw_input().split())
number = a
while(a>=b):
	d = a/b
	number = number + d
	a = d + int(a%b)
print number
