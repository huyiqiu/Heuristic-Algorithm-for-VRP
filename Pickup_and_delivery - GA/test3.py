def plus(a, b):
    return a+b
def minus(a, b):
    return a-b

def func(prolem, a, b):
    if prolem == 1:
        f = plus(a, b)
    else:
        f = minus(a, b)
    return f

print(func(1,2,3))
print(func(0, 2, 3))