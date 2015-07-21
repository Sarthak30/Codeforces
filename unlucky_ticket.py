n = int(raw_input())
num = raw_input()
num1 = sorted(list(num[:n]))
num2 = sorted(list(num[n:]))
if num1==num2:
	print "NO"
	exit()
count = [0,0]
for i in range(n):
	if(num1[i]<num2[i]):
		count[0] = count[0]+1
	if(num1[i]>num2[i]):
		count[1] = count[1]+1
if count[0] == n or count[1] == n:
	print "YES"
else:
	print "NO"
	
