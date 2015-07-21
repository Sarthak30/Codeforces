count = 0; 
a = [] 
n = int(raw_input()) 
num = map(int,raw_input().split())
for i in range(n):
	if(num[i]==1):
		a.append(-1)
		count = count + 1
	else:
		a.append(1)
  
m = -2
s = 0;  
for i in range(n):
	s = s + a[i]
	if s>m:
		m = s
	if s<0:
		s = 0
print m+count
