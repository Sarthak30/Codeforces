a = str(raw_input())
b = ""
for i in a:
	i
	if ((len(b)==0) or (int(b)==0)) and (i=="9"):
		b = b+i
	elif(int(i)>4):
		b = b+str(9-int(i))
	else:
		b = b+i
print b
