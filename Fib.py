def fib(n):
    var1 = 0
    var2 = 1
    sum = n
    for i in range(n):
        if i == 0:
            continue
        sum = var1+ var2
        var1 = var2
        var2 = sum
    return sum

print fib(9)

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
print F(9)n