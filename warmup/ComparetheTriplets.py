def compareTriplets(a, b):
    al=0
    bo=0
    n=int(len(a))
    for h in range(n):
        if a[h]>b[h]:
            al = al + 1
        if a[h]<b[h]:
            bo= bo + 1
    return al , bo