a = str(raw_input())
b = str(raw_input())
c = str(raw_input())
d = a+b
if not(len(d)==len(c)):
	print "NO"
else:
	e = {' ':0, 'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
	f = {' ':0, 'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
	for i in range(0,len(d)):
		e[d[i]] = e[d[i]]+1
		f[c[i]] = f[c[i]]+1
	if(e==f):
		print "YES"
	else:
		print "NO"
	
