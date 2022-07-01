k=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
s=0
for i in a:
    if m<=i and n>=i:
        continue
    else:
        s=s+i
print(s)     
        