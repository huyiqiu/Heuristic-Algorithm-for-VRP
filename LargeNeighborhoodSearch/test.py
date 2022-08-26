from operator import itemgetter, attrgetter
a = []
b= 1
a.append([b,7])
a.append([3,5])
a.append([2,8])
a = sorted(a, key=itemgetter(1), reverse=True)
print(a)
print(a[0][0])
