n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    cmd=input().split()
    if cmd[0]=='pop':
        s.pop()
    if cmd[0]=='remove':
        s.remove(int(cmd[1]))
    if cmd[0]=='discard':
        s.discard(int(cmd[1]))
tot=0
for z in s:
    tot=tot+z
print(tot)