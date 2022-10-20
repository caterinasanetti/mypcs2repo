from collections import Counter
x=int(input())
stock=list(input().split())
pair=Counter(stock)
n=int(input())
money=0
for z in range(n):
    size , price =input().split()
    if pair[size] != 0:
        money += int(price)
        pair[size] -= 1
    if pair[size]<=0:
        money += 0
print(money)