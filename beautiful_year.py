a = int(raw_input())
flag = 0
while(flag==0):
	a = a+1
	c = list(set(str(a)))
	if(len(c)==4):
		print a
		flag=1
	
