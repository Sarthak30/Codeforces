a = int(raw_input())
count = 0
for i in range(0,a):
	b = raw_input()
	c = b.split()
	c = map(int, c)
	if(sum(c)>=2):
		count = count + 1
print count 
