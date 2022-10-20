a =int(input())
b=int(input())
m=int(input())
if a>=1 and a<=10:
    if b>=1 and b<=10:
        if m>=2 and m<=1000:
            power = pow(a,b)
            mpower= pow(a,b,m)
            print(power)
            print(mpower)