n=int(input())
a=list(map(int,input().split()))
a=set(a)
b=0
for i in a:
    if i%2==0:
        b=b+i
print(b)