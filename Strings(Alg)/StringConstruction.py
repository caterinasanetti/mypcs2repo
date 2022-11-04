def stringConstruction(s):
    a=[]
    for i in s:
        if i not in a :
            a.append(i)
    return len(a)