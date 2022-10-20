from itertools import permutations
w,l=input().split()
w= sorted(w)
l = int(l)
if l>0 and l<len(w):
    perm=list(permutations(w,l))
    for c in perm:
        print("".join(c))
