def quickSort(arr):
    pivot=arr[0]
    r=[]
    c=[]
    l=[]
    for i in range(len(arr)):
        if arr[i]>pivot:
            r.append(arr[i])
        elif arr[i]==pivot:
            c.append(arr[i])
        else:
            l.append(arr[i])
    u=[]
    for x in l:
        u.append(x)
    for y in c:
        u.append(y)
    for z in r:
        u.append(z)
    return u