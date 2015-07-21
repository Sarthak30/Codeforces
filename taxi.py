a = int(raw_input())
b = raw_input()
c = (b.split())
c = map(int,c)
c.sort(reverse = True)
x = len(c)
count = 0
i=0
j=len(c)-1
while(i<=j):
	count=count+1
	s = 4 - c[i]
	while (c[j]<=s and i<=j):
		s = s-c[j]
		j=j-1	
	i=i+1 
print count

