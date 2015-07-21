a = int(raw_input())
b = map(int,raw_input().split())
s, t = map(int,raw_input().split())
s = s-1
t = t-1
g = []
c = sum(b[s:])+sum(b[:t])
if not(c==0):
	g.append(c)
d = sum(b[t:])+sum(b[:s])
if not(d==0):
	g.append(d)
e = sum(b[s:t])
if not(e==0):
	g.append(e)
f = sum(b[t:s])
if not(f==0):
	g.append(f)
if(s==t):
	print "0"
else:
	print min(g)
