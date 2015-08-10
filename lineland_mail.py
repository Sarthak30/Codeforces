raw_input()
a=map(int,raw_input().split())
print a[1]-a[0],a[-1]-a[0]
for i in range(1,len(a)-1):
    print min(a[i]-a[i-1],a[i+1]-a[i]),max(a[i]-a[0],a[-1]-a[i])
print a[-1]-a[-2],a[-1]-a[0]
