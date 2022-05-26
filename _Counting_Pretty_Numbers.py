n=int(input())
for j in range(n):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        k=i%10
        i=i//10
        if(k==3 or k==2 or k==9):
            c+=1
        
    print(c)
    