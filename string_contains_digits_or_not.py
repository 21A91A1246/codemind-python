t=int(input())
for i in range(t):
    s=input()
    c=0
    for i in s:
        if i.isdigit():
            print("Yes")
            break
    else:
        print("No")