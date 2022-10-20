from itertools import product
frlin=(input().split())
a=[]
for i in frlin:
    a.append(int(i))
seclin=(input().split())
b=[]
for i in seclin:
    b.append(int(i))
print(*product(a, b))