def miniMaxSum(arr):
    minimum=min(arr)
    maximum=max(arr)
    minsum=sum(arr)-maximum
    maxsum= sum(arr)-minimum
    print(minsum,maxsum )