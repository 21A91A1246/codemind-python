s=int(input())
b=list(map(int,input().split()))
for i in range(s):
    if b[i]%2!=0:
        print(b[i],end=' ')
for i in range(s):
    if b[i]%2==0:
        print(b[i],end=' ')