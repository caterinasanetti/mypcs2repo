def diagonalDifference(arr):
    fd=0
    sd=0
    for h in range(0,len(arr)):
        fd+= arr[h][h]
        sd+=arr[h][(len(arr)-h-1)]
    tot= abs(fd-sd)
    return tot
        