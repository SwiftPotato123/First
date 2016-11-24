import os
root = '/home/dev/'
y = os.listdir(root)
print y
for x in y:
    n = os.path.join(root,x)
    if os.path.isdir(n) == True:
        print n
    else:
        print 'Not directory'