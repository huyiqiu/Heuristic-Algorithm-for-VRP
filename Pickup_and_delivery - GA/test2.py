import random
import copy
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
def exchange_move(a, b):
    p1, p2 = random.sample(range(len(a)), 2)
    if p1 > p2:
        p1, p2 = p2, p1
    cuta, cutb = a[p1:p2], b[p1:p2]
    tempa, tempb = copy.deepcopy(a), copy.deepcopy(b)
    print(cuta, cutb)
    for i in tempa:
        if i in cutb:
            a.remove(i)
    for i in cutb:
        a.append(i)
    for i in tempb:
        if i in cuta:
            b.remove(i)
    for i in range(len(cuta)):
        b.insert(0, cuta[len(cuta)-i-1])

exchange_move(a, b)
print(a, b)