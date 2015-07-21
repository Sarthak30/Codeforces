a = int(raw_input())
b = map(int,raw_input().split())
c = 0
count = 0
i = 0
while(i<a):
	c = c+b[i]
	if(c<0):
		count = count + 1
		c=c-1
		if(c<0):
		    c = 0
	i = i+1
print count
