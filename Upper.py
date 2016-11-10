def upper(s):
    o=""
    for l in s:
        if ord(l)>=ord("A") and ord(l)<=ord("Z"):
            n=ord(l)+32
            o= o+chr(n)
        else:
            o= o+l
    return o

s1=upper("Hello World!")
print s1