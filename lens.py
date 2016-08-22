def lens(s1, s2):
    s1, s2 = ((s1,s2) if (len(s1)<len(s2)) else (s2, s1))
    i = 0
    j = len(s1)
    bestj = 0
    while (i<len(s1)) and (len(s1)-i>bestj):
        temp = s1[i:]
        j = len(temp)
        while j>0:
            if temp[:j] in s2:
                if j > bestj:
                    bestj=j
                break
            j-=1
        i+=1
    return bestj



if __name__ == '__main__':
    print lens('abgoogle', 'cbagoogle')
    print lens('agoogle', 'bgoogle')
    print lens('googlea', 'googleddd')
    print lens('abc', 'google')
