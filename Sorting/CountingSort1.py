def countingSort(arr):
    freq=[0]*100
    for i in arr:
        freq[i]+= 1
    return freq