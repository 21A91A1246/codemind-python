n=int(input())
a=list(map(int,input().split()))
s1=a[0]
s2=0
for i in range(1,n):
    if i%2==0:
        s1=s1+a[i]
    else:
        s2=s2+a[i]

print(abs(s1-s2))