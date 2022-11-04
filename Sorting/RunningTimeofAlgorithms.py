def runningTime(arr):
    count=0
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]>arr[i]:
                count +=1
    return count