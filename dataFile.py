f = open('/home/dev/Downloads/file1.txt', 'w')
f.write('This is my first file\n')
f.write('This is my first file\n')
f.write('This is my first file\n')
f.write('This is my first file\n')
f.write('This is my first file\n')
f.write('This is my first file\n')
f.write('This is my first file\n')
f.close()

with open('/home/dev/Downloads/file1.txt', 'r') as f:
    read = f.readlines()

print read

counter = 0.0
with open('/home/dev/Downloads/file1.txt', 'w') as f:
    for x in read:

        if counter % 2.0 == 0.0:
            print counter, x
            f.write('x y z\n')
        else:
            f.write(x)
        counter = counter + 1
f.close()
y = open('/home/dev/Downloads/file1.txt', 'a')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.write('Hello\n')
y.close()






