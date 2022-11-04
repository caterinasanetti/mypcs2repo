def closestNumbers(arr):
    arr.sort()
    res= []
    minimum = 999999999
    for i in range(1, len(arr)): 
        diff = arr[i] - arr[i-1]
        if diff == minimum: 
            res.extend([arr[i-1], arr[i]])
        if diff < minimum: 
            minimum = diff 
            res = [arr[i-1], arr[i]]
        else:
            continue
    return res