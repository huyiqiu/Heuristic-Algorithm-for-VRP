import random
a = [1,2,3,4,5,6,7,8,9,10]
p1, p2, p3, p4 = random.sample(a, 4)
print(p1, p2, p3, p4)
a.remove(p1)
a.remove(p2)
a.remove(p3)
a.remove(p4)
print(a)