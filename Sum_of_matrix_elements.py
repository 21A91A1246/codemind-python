a=int(input())
b=int(input())
s=0
for i in range(a):
    
    d=list(map(int,input().split()))
    s=s+sum(d)
print(s)
