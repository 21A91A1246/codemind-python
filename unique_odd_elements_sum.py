n=int(input())
a=list(map(int,input().split()))
a=set(a)
b=[]
for i in a:
    if i%2!=0:
        b.append(i)
print(sum(b))