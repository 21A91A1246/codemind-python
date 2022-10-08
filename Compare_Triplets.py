import sys

def score(a, b):
    x = 0
    y = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            x += 1
        elif a[i] < b[i]:
            y += 1
    return x, y

a=list(map(int,input().split()))
b=list(map(int,input().split()))

print('%d %d' % score(a,b))