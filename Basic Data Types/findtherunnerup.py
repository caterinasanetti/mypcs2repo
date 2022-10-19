if __name__ == '__main__':
    n = int(input())
    a=[]
    arr=list(map(int, input().split()))
    arr2=set(arr)
    maxi=max(arr2)
    for i in arr:
        if i!= maxi:
            a.append(i)
    b=set(a)
    print(max(b))