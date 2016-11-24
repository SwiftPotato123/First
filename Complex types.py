l = []
l.append(1)
l.append(2)
l.append(3)
l.append(3)
l.append(2)
print l

d={}
d[1]='a'
d[2]='b'
print d
print l[1]
l[1]=5
print l[1]
print d.get(6)
s = set(l)
print s