def findMedian(arr):
    arr.sort()
    n =len(arr)
    indexn= int(((n+1)/2)-1)
    median = arr[indexn]
    return(median)