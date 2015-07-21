n, b, p = map(int,raw_input().split())
bl = b
pl = p
w = 0
d = map(int,raw_input().split())
for i in d:
	flag = 0
	if(i==1):
		if bl is not 0:
			bl = bl-1
			flag = 1
	elif(i==2):
		if pl is not 0:
			pl = pl-1
			flag = 1
		elif bl is not 0:
			bl = bl-1
			flag = 1
	if(flag==0):
		w = w+1
print w
