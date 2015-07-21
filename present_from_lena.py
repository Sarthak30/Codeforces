inp = int(raw_input())
k = inp - 1
 
def generate(n):
    return [' ' for i in range(inp - n + 1)] \
        + [str(i) for i in range(n)] + [str(i) for i in range(n-1)][::-1]
 
for i in range(inp + 1):
    print " ".join(generate(i + 1))
 
while(k >= 0):
    print " ".join(generate(k + 1))
    k -= 1
