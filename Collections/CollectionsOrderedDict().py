from collections import OrderedDict
od=OrderedDict()
n=int(input())
for x in range(n):
    *name,price =input().split()
    name=" ".join(name)
    if name  not in od:
        od[name] =int(price)
    else:
        od[name] += int(price)

for name,price in od.items():
    print(name,price)