s=input()
a=input()
k=0
for i in range(len(s)):
    if s[i]==a:
        k=1
        break
if k==0:
    print(False)
else:
    print(True)
    print(i)