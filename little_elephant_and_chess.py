a = 'BWBWBWBW'
b = 'WBWBWBWB'
for i in range(8):
	c = raw_input()
	if(c==a or c==b):
		continue
	else:
		print "NO"
		exit()
print "YES"
