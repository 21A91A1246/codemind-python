n=int(input())
a=list(map(int,input().split()))
a=set(a)
a=list(a)
if(len(a)<3):
    print(max(a))
elif(len(a)>=3):
    for i in range(2):
        j=max(a)
        a.remove(j)
    print(max(a))    