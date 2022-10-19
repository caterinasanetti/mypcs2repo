if __name__ == '__main__':
    n=int(input())
    nested=[]
    marks=[]
    for i in range(n):
        name=input()
        mark=float(input())
        marks.append(mark)
        nested.append([name , mark])
ordered=sorted(set(marks))
minus=(min(ordered))
ordered.remove(minus)
newmin=(min(ordered))
student=[]
for t in nested:
    if newmin == t[1]:
        student.append(t[0])
student.sort()
for j in student:
    print(j)