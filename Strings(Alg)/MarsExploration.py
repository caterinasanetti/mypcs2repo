def marsExploration(s):
    f="SOS"
    o = []
    c=[]
    while s:
        o.append(s[:3])
        s = s[3:]
    for tokens in o:
        if tokens != f:
            c.append(tokens)
    count= 0
    for i in range(len(c)):
        if c[i][0] != "S":
            count += 1
        if c[i][1] != "O":
            count += 1
        if c[i][2] != "S":
            count += 1
    return count