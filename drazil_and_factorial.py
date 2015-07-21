a = int(raw_input())
b = str(raw_input())
b = b.replace("0","")
b = b.replace("1","")
b = b.replace("4","322")
b = b.replace("6","53")
b = b.replace("8","7222")
b = b.replace("9","7332")
b = sorted(b,reverse = True)
print "".join(b)


