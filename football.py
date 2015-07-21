a = str(raw_input())
count1 = 0
count0 = 0
flag = 0
for i in range(0,len(a)):
	if(a[i]=='0'):
		count0 = count0+1
		count1 = 0
	else:
		count1 = count1+1
		count0 = 0
	if(count1 == 7 or count0 == 7):
		print "YES"
		flag = 1
		break 
if(flag == 0):
	print "NO"
