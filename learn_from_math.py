def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True
a = int(raw_input())
flag = 0
if(a%2==0):
	flag = 1
	if(is_prime(a/2)):
		print str((a/2)+1)+" "+str((a/2)-1)
	else:
		print str(a/2)+" "+str(a/2)
if(flag == 0):
	for i in range(4,(a/2)+1):
		j = a-i
		if not(is_prime(i)):
			if not(is_prime(j)):
				print str(i)+" "+str(j)
				break
