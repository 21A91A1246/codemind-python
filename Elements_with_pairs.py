n=int(input())
a=list(map(int,input().split()))
if n%2==0:
        print(*a)
else:
    print(*a,end=' 0')