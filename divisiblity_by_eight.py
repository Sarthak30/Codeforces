import re
n = raw_input()
for i in range(0, 1000,8):
    r = '.*'.join(['']+list(str(i))+[''])
    if re.search(r,n):
        print("YES")
        print(i)
        exit()
print("NO")
