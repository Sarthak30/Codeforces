n=input()
a=map(int,raw_input().split())
index=sorted(range(len(a)), key=lambda k: a[k])
a=sorted(a)
for i in range(len(index)):
    index[i]+=1


i=1
count =1
ans=list()


ans.append(index)


while i <len(a):
    if a[i]==a[i-1]:
        index[i],index[i-1]=index[i-1],index[i]
        ans.append(list(index))
        index[i],index[i-1]=index[i-1],index[i]
        count+=1
        if count==3:
            break
    i+=1


if count==3:
    print "YES"
    for i in range(3):
        for j in range(len(ans[i])):
            print ans[i][j],
        print

else:
    print "NO"
