def isAnagram(s: str, t: str) -> bool:
    for i in s:
        if s.count(i) == t.count(i):
            cond = True
        else:
            cond = False
            break
    if cond == True:
        if len(s) == len(t):
            cond = True
        else:
            cond = False
    return cond