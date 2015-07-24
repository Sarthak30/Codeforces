raw_input()
a = 'vaporeon'
b = 'jolteon'
c = 'flareon'
d = 'espeon'
e = 'umbreon'
f = 'leafeon'
g = 'glaceon'
h = 'sylveon'
b1 = c1 = e1 = f1 = g1 = h1 = 0
x = raw_input()
l = len(x)
if(l == 6):
	print d
	exit()
elif(l == 8):
	print a
	exit()
else:
	i = 0
	while(i<7):
		y = x[i]
		if(x[i] == '.'):
			i = i+1
			continue
		if(x[i] == b[i] and b1 == 0):
			b1 = 0
		else:
			b1 = 1
		if(x[i] == c[i] and c1 == 0):
			c1 = 0
		else:
			c1 = 1
		if(x[i] == e[i] and e1 == 0):
			e1 = 0
		else:
			e1 = 1
		if(x[i] == f[i] and f1 == 0):
			f1 = 0
		else:
			f1 = 1
		if(x[i] == g[i] and g1 == 0):
			g1 = 0
		else:
			g1 = 1
		if(x[i] == h[i] and h1 == 0):
			h1 = 0
		else:
			h1 = 1
		i = i+1
if(b1 == 0):
	print b
elif(c1 == 0):
	print c
elif(e1 == 0):
	print e
elif(f1 == 0):
	print f
elif(g1 == 0):
	print g
else:
	print h
		
