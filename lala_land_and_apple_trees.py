n = int(raw_input())
ne = []
po = []
for i in range(n):
	x, a = map(int,raw_input().split())
	if(x<0):
		ne.append((x,a))
	elif(x>0):
		po.append((x,a))
ne.sort(reverse = True)
po.sort()
neg = [y for x,y in ne]
pos = [y for x,y in po]
ln = len(neg)
lp = len(pos)
if(ln==lp or abs(ln-lp)==1):
	print sum(pos)+sum(neg)
elif(ln>lp):
	print sum(neg[:lp+1])+sum(pos)
else:
	diff = lp-ln
	print sum(neg)+sum(pos[:ln+1])

