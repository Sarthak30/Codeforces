a = int(raw_input())
even = 1
if(a%2==0):
	print (a/2)*a
else:
	print (((a+1)/2)*(a+1))-a
for i in range(a):
	b = ""
	if(even == 1):
		for i in range(0,a,2):
			b = b + "C."
		if not(a%2==0):
			b = b[:-1]
		even = 0
		print b
	elif(even == 0):
		for i in range(1,a,2):
			b = b + ".C"
		if not(a%2==0):
			b = b + "."
		even = 1
		print b
		
