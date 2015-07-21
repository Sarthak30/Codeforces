a = map(int,raw_input().split())
b = {}
for i in a:
	if i not in b:
		b[i]=1
	else:
		b[i]=b[i]+1
flag = 0
for i in b:
	if b[i]>3:
		flag = 1
		break	
if flag==0:
	print "Alien"
else:
	b[i] = b[i]-4
	if(b[i]==0):
		del b[i]
	if len(b)==1:
		print "Elephant"
	else:
		print "Bear"
