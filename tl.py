raw_input()
n = map(int,raw_input().split())
m = map(int,raw_input().split())
p = -1
for i in range(max(n),min(m)):
	if(2*min(n)<=i):
		p = i
		break
print p		
