n=int(input())
for i in range(n):
    a=input()
    c=a[::-1]
    if c!=a:
        print("NO")
        continue
    if c==a:
        print("YES",end=' ')
    if (len(a))%2==0:
        print("EVEN")
    if (len(a))%2!=0:
        print("ODD")
    
    