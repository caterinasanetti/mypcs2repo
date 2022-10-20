n=int(input())
classification=input().split()
Mark=classification.index('MARKS')
lst=[]
for i in range(n):
    split=(input().split())
    marks=int(split[Mark])
    lst.append(marks)
s=0
for i in lst:
    s += i
print(s/n)