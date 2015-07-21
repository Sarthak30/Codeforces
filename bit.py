a = int(raw_input())
x = 0
for i in range(0,a):
	b = str(raw_input())
	if(b=="X++" or b=="++X"):
		x=x+1
	elif(b=="X--" or b=="--X"):
		x=x-1
print x
