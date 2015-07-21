a=[map(int, raw_input().split()) for i in [0]*2][1]
m=sorted(a)
i=0
while i<len(a)-1:
    if a[i]>a[i+1]:break
    i+=1
j=i
while j<len(a)-1:
    if a[j]<a[j+1]:break
    j+=1
b=a[:i]+a[i:j+1][::-1]+a[j+1:]
if b==m:print"yes\n",i+1,j+1
else:print"no"
