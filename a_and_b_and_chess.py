sw=0
sb=0
for i in range(0,8):
	a = str(raw_input())
	for i in a:
		if(i == 'Q'):
			sw=sw+9
		elif(i=='R'):
			sw=sw+5
		elif(i=='B'):
			sw=sw+3
		elif(i=='N'):
			sw=sw+3
		elif(i=='P'):
			sw=sw+1
		if(i == 'q'):
			sb=sb+9
		elif(i=='r'):
			sb=sb+5
		elif(i=='b'):
			sb=sb+3
		elif(i=='n'):
			sb=sb+3
		elif(i=='p'):
			sb=sb+1
if(sw>sb):
	print 'White'
elif(sb>sw):
	print 'Black'
else:
	print 'Draw'
			
