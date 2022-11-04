def hackerrankInString(s):
    s.lower()
    a=[]
    for i in s:
        if (i=="h" or i=="a" or i=="c" or i=="k" or i=="e" or i=="r" or i=="n"):
            a.append(i)
    target=['h','a','c','k','e','r','r','a','n','k']
    for i in a:
        if target:
            if i== target[0]:
                target.pop(0)
    if len(target) == 0:
        return("YES")
    else:
        return("NO")