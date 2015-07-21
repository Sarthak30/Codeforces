n = list(str(raw_input()))
x = -1
for i in range(len(n)):
	if(int(n[i])%2==0):
		if(n[i]>n[-1]):
			x = i
		else:
			x = i
			break
if(x!=-1):
	n[x],n[-1] = n[-1],n[x]
	print ''.join(n)
else:
	print '-1'
