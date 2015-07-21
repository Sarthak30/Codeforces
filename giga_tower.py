m = int(raw_input())
for i in range(100000):
	m = m+1
	a = str(m)
	if a.find('8') is not -1:
		break
print i+1
