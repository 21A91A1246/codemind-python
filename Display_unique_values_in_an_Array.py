n=int(input())
a=list(map(int,input().split()))
k=1
for i in a:
    if a.count(i)==1:
        print(i,end=' ')
        k=0
        
    
if k==1:
    print('-1')