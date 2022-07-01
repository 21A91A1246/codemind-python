b=int(input())
s=list(map(int,input().split()))

for i in range(b):
    if s[i]%2==0:
        print(s[i],end=' ')
for i in range(b):
    if s[i]%2!=0:
        print(s[i],end=' ')
    
    