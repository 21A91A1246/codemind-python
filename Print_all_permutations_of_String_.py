from itertools import permutations
n=input()
k=permutations(n)
for i in k:
    for j in i:
        print(j,end="")
    print()    