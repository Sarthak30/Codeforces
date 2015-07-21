n = int(raw_input())
d = map(int,raw_input().split())
c5 = d.count(5)
c0 = d.count(0)
num = ''
flagc5 = 1
if(c5/9>0):
	flagc5 = 0
	a = c5/9
	a = a*9
if(flagc5==0 and c0 is not 0):
	for i in range(a):
		num = num+'5'
	for j in range(c0):
		num = num+'0'
	print num
else:
	if(c0>0):
		print '0'
	else:
		print '-1'
