n = int(raw_input())
arr = []
for i in xrange(n):
    var = map(int,raw_input().split())
    arr.append(tuple(var))

arr.sort()
pre = min(arr[0][0],arr[0][1])
for i in xrange(1,n):
    temp = min(arr[i][0],arr[i][1])
    if temp<pre:
        pre = max(arr[i][0],arr[i][1])
    else:
        pre = temp

print pre
