def timeConversion(s):
    for j in s:
        if j=='A'and s[:2]=="12":
            return("00"+ s[2:-2])
        elif j=="A":
            new=s[:-2]
            return new
        elif j=="P" and s[:2]=="12":
            return(s[:-2])
        elif j=="P":
            timm=s[:-2]
            return str(int(timm[:2])+12)+s[2:8]