n=int(input())
a=list(map(int,input().split()))
f=0
s=[]
for i in range(n):
    if a[i]==a.count(a[i]) and a[i] not in s:
        s.append(a[i])
        f+=1
print(f)        