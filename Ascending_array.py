n=int(input())
a=list(map(int,input().split()))
c=sorted(set(a))
b=a[::1]
if c==b:
    print('yes')
else:
    print('no')
