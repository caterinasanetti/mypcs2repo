from itertools import combinations_with_replacement
w,l = input().split()
w=sorted(w)
l=int(l)
if l>0 and l<=len(w):
    combr=list(combinations_with_replacement(w,l))
    for s in combr:
        print(("").join(s))