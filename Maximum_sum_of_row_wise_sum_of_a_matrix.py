a,b=map(int,input().split())
p=[]
for i in range(a):
    s=list(map(int,input().split()))
    sa=sum(s)
    p.append(sa)
print(max(p))
    