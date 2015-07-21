n=input()
r=map(len, filter(lambda x:len(x),raw_input().replace(' ','').split('0')))
print max(sum(r)+len(r)-1,0)
