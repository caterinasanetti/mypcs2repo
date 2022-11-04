def plusMinus(arr):
    pos=[]
    neg=[]
    zero=[]
     
    for i in arr:
        if i > 0:
            pos.append(i)
        if i==0:
            zero.append(i)
        if i<0:
            neg.append(i)
            
    proppos = len(pos)/len(arr)
    print(f"{proppos:.6f}")
    propneg = len(neg)/len(arr)
    print(f"{propneg:.6f}")
    propzero = len(zero)/len(arr)
    print(f"{propzero:.6f}")
