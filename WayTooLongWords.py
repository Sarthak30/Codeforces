i = int(raw_input())
for x in range(0,i) : 
	a = raw_input()
	if(len(a)>10) : 
		print a[0]+str(len(a)-2)+a[len(a)-1]
	else : 
		print a
	
