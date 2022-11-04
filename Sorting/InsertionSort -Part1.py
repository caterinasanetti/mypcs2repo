def insertionSort1(n, arr):
    for i in range(1, n):
        key = arr[i]
        while i> 0 and arr[i-1] > key:
            arr[i] = arr[i-1]
            i -= 1
            print(*arr)
        arr[i] = key
    print(*arr)