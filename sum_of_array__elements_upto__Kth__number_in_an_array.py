n=int(input())
a=list(map(int,input().split()))
x=int(input())
b=a[:x:1]
print(sum(b))
