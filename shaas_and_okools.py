R = lambda:map(int, raw_input().split())
n = R()
seq =[0]+ R() +[0]
for i in range(input()):
    x, y =R()
    seq[x-1]+=y-1
    seq[x+1]+=seq[x]-y
    seq[x]=0
print '\n'.join(map(str,seq[1:-1]))
