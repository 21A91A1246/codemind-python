s=input()
s=s.split()
s=sorted(s)
s.sort(key=len)
print(*s)
    