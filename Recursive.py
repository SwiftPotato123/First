import os


def r(p):
    if os.path.isdir(p):
        print 'Directory', p
        content = os.listdir(p)
        for x in content:
            r(os.path.join(p, x))
    else:
        print 'file', p


root = '/home/dev/'
r(root)
