from itertools import combinations
w,l = input().split()
w=sorted(w)
l=int(l)
if l>0 and l<len(w):
    for h in range(1,l+1):
        a= (list(combinations(w,h)))
        for i in a:
            print(("").join(i))