def lower(s):
    o = ""
    for l in s:
        if ord("A") <= ord(l) <= ord("Z"):
            n = ord(l) + 32
            o += chr(n)
        else:
            o = o + l
    return o


s1 = lower("Hello World!")
print s1
