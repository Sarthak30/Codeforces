a = int(raw_input())
c = map(int,raw_input().split())
c.sort(reverse = True)
d = sum(c)
d = int(d/2)+1
sumi = 0
i = 0
for j in c:
	sumi = sumi+j
	i = i+1	
	if(sumi>=d):
		break 
print i
