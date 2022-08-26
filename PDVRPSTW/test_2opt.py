import random

solotion = [3,4,5,6,7,8,9]
p1, p2 = random.sample(range(len(solotion)), 2)
if p1 > p2:
    p1, p2 = p2, p1
cut = solotion[p1:p2]
for i in cut:
    if i in solotion:
        solotion.remove(i)
for i in range(len(cut)):
    solotion.insert(p1, cut[i])
