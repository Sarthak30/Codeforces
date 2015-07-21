a = str(raw_input())
count = 0
for i in a:
	if(i=='4' or i=='7'):
		count=count+1
d = set(str(count))
d = list(d)
if(count==4):
	print "YES"
elif(count==7):
	print "YES"
elif(d[0]=='4' and d[1]=='7'):
	print "YES"
else:
	print "NO"
