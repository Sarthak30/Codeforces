a = int(raw_input())
b = map(int,raw_input().split())
x = []
j = 0
z = []
for i in range(sum(b)+1):
	if(i<b[j]):
		z.append(i)
	else:
		x.append(z)
		j = j + 1
		z = []
print x
c = int(raw_input())
d = map(int,raw_input().split())
