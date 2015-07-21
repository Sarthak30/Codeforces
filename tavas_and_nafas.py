a = {
		0:'',
		1:'one',
		2:'two',
		3:'three',
		4:'four',
		5:'five',
		6:'six',
		7:'seven',
		8:'eight',
		9:'nine',
		10:'ten',
		11:'eleven',
		12:'twelve',
		13:'thirteen',
		14:'fourteen',
		15:'fifteen',
		16:'sixteen',
		17:'seventeen',
		18:'eighteen',
		19:'nineteen'
		}
b = {
		2:'twenty',
		3:'thirty',
		4:'forty',
		5:'fifty',
		6:'sixty',
		7:'seventy',
		8:'eighty',
		9:'ninety'
	}
n = int(raw_input())
if(n==0):
	print 'zero'
elif(n<20):
	print a[n]
else:
	x = n/10
	y = n%10
	if not(y==0):
		print b[x]+"-"+a[y]
	else:
		print b[x]
	
