n = raw_input()
ans = [2,7,2,3,3,4,2,5,1,2]
prod = 1
for i in n:
    prod *= ans[int(i)]
print prod
