n=int(input())
for i in range(n):
    k=int(input())
    a=list(map(int,input().split()))
    a=sorted(a)
    k=1
    for j in a:
        if j!=k:
            print(j-1)
            break
        k+=1
    if(k>len(a)):
       print(k)    