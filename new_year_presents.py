input()
k=map(int,raw_input().split())
print"PRL"*k[0]+"".join("R"+i*"PLR"for i in k[1:])
