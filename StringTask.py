a = raw_input()
a = a.lower()
b=''
for i in a : 
	if( i=='a' or i=='o' or i=='y' or i=='e' or i=='u' or i=='i') : 
		a = 1
	else : 
		b=b+'.'+i
print b
