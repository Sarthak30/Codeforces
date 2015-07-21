import math
 
n = input()
 
ans=["","Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
 
i= int(math.log(math.ceil(n*1.0/5),2))
 
ans_index= int(math.ceil((n-(2**i -1)*5 )/(2**i*1.0)))
 
print ans[ans_index]
