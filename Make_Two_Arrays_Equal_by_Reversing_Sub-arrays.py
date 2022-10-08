x=int(input())
s=list(map(int,input().split()))
y=int(input())
b=list(map(int,input().split()))
if sorted(s)==sorted(b):
    print(True)
else:
    print(False)