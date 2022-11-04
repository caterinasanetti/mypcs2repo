def alternatingCharacters(s):
    count = 0
    for i in range(0,len(s)-1):
        if s[i+1] == s[i]:
            count += 1
        else:
            count += 0
    return count