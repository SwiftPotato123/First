import os
root = '/home/dev/'
y = os.listdir(root)
print y
for x in y:
    n = os.path.join(root,x)
    if os.path.isdir(n):
        print n
    else:
        print 'Not directory'