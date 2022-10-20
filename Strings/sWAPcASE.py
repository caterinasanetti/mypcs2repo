def swap_case(s):
    f = ""
    for a in s:
        if a.islower():
            a=a.upper()
        else:
            a=a.lower()
        f +="".join(a)        
    return f