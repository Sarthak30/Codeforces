a = int(raw_input())
b = map(int,raw_input().split())
c = 0
energy = 0
x = 0
for i in range(a):
	energy = energy+(x-b[i])
	if(energy<0):
		c = c+abs(energy)
		energy = 0
	x = b[i]
print c
