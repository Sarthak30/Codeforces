a = int(raw_input())
flag=1
if(a%4==0):
	print "YES"
	flag=0
elif(a%7==0):
	flag=0
	print "YES"
else: 
	for i in range(44,a+1):
		d=[]
		d = set(str(i))
		if (d==set(['4', '7'])):
			if(a%i==0):
				flag=0
				print "YES"
				break
		elif(d==set(['4'])):
			if(a%i==0):
				flag=0
				print "YES"
				break
		elif(d==set(['7'])):
			if(a%i==0):
				flag=0
				print "YES"
				break
if(flag==1):
	print "NO"

