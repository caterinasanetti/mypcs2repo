a =int(input())
b=int(input())
c=int(input())
d=int(input())
if a>=1 and a<=1000:
    if b>=1 and b<=1000:
        if c>=1 and c<=1000:
            if d>=1 and d<=1000:
                f= pow(a,b)
                g= pow(c,d)
                result=int(f+g)
print(result)  