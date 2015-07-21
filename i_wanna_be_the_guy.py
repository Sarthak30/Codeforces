n = int(raw_input())
c = []
for i in range(1,n+1):
	c.append(i)
a = map(int,raw_input().split())
b = map(int,raw_input().split())
a.pop(0)
b.pop(0)
a.extend(b)
a = list(set(a))
a.sort()
if(a==c):
	print "I become the guy."
else:
	print "Oh, my keyboard!"
