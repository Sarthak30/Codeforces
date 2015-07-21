x = []
n = int(raw_input())
for j in range(n):
	a = str(raw_input())
	if(a=='pwd'):
		if(len(x)==0):
			print '/'
		else:
			print '/'+'/'.join(x)+'/'
	else:
		a = a[3:]
		b = map(str,a.split('/'))
		if(a[0]=='/'):
			x = []
		for i in b:
			if(len(i) is not 0):
				if(i == '..'):
					x.pop(len(x)-1)
				else:
					x.append(i)
			
