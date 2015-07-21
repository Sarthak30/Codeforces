x1,y1,x2,y2 = map(int,raw_input().split())
if (not(x1 == x2) and not(y1 == y2) and not(abs(x1 - x2) == abs(y1 - y2))):
    print "-1"
elif (x1 == x2):
    print str((x1)+(abs(y1 - y2))) + " " + str(y1) + " " + str((x2)+(abs(y1 - y2))) + " " + str(y2)
elif (y1 == y2):
   print str(x1) + " " + str(y1 + abs(x1 - x2)) + " " + str(x2) + " " + str(y2 + abs(x1 - x2))
else:
   print str(x1)+" "+str(y2)+" "+str(x2)+" "+str(y1)
