a = int(raw_input())
b = str(raw_input())
c = str(raw_input())
count = 0
for i in range(a):
	x = int(b[i])
	y = int(c[i])
	count = count+min(abs(x-y),10-abs(x-y))
print count
