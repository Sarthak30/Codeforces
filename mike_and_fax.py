def palindrome(n):
	return n==n[::-1]
s = raw_input()
n = int(raw_input())
if(len(s)%n != 0):
	print "NO"
	exit()
a = len(s)/n
flag = 0
for i in range(n):
	b = s[:a]
	s = s[a:]
	if(len(b)==a and palindrome(b)==True):
		continue
	else:
		flag = 1
		break
if flag is 1:
	print "NO"
else:
	print "YES"
