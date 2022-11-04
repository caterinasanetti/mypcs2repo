def insertionSort2(n, arr):
    for index in range(1,n):
        for compvalue in range(index):
            if arr[compvalue] > arr[index]:
                temp = arr[compvalue]
                arr[compvalue] = arr[index]
                arr[index] = temp
        print(*arr)