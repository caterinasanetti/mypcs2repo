def staircase(n):
    s=[]
    base ='#'
    for i in range(1,n+1):
        s.append(' '*(n-i)+base*(i))
    for j in s:
        print(j)
       