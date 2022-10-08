n=int(input())
s=list(map(int,input().split()))
l=0;r=1;c=0;ma=0
while r<n:
    if s[l]>s[r]:
        l=r
        r+=1
    else:
        c=abs(s[r]-s[l])
        r+=1
        l+=1
        ma=ma+c
print(ma)