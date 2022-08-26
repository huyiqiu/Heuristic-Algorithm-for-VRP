"""berlin52的"""

import numpy as np
import matplotlib.pyplot as plt
import random
import copy
from operator import itemgetter, attrgetter
from pre_ans import create_preans
#berlin52
city = [
[ 565,575 ],[ 25,185 ],[ 345,750 ],[ 945,685 ],[ 845,655 ],
[ 880,660 ],[ 25,230 ],[ 525,1000 ],[ 580,1175 ],[ 650,1130 ],
[ 1605,620 ],[ 1220,580 ],[ 1465,200 ],[ 1530,5 ],
[ 845,680 ],[ 725,370 ],[ 145,665 ],
[ 415,635 ],[ 510,875 ],[ 560,365 ],[ 300,465 ],[ 520,585 ],[ 480,415 ],
[ 835,625 ],[ 975,580 ],[ 1215,245 ],[ 1320,315 ],[ 1250,400 ],[ 660,180 ],
[ 410,250 ],[ 420,555 ],[ 575,665 ],[ 1150,1160 ],[ 700,580 ],[ 685,595 ],
[ 685,610 ],[ 770,610 ],[ 795,645 ],[ 720,635 ],[ 760,650 ],[ 475,960 ],
[ 95,260 ],[ 875,920 ],[ 700,500 ],[ 555,815 ],[ 830,485 ],[ 1170,65 ],
[ 830,610 ],[ 605,625 ],[ 595,360 ],[ 1340,725 ],[ 1740,245 ]
	]
#中国省会
city2 = [(1304,2312),(3639,1315),(4177,2244),(3712,1399),(3488,1535),
                 (3326,1556),(3238,1229),(4196,1004),(4312,790),(4380,570),
                 (3007,1970),(2562,1756),(2788,1491),(2381,1676),(1332,695),
                 (3715,1678),(3918,2179),(4061,2370),(3780,2212),(3676,2578),
                 (4029,2838),(4263,2931),(3429,1908),(3507,2367),(3394,2643),
                 (3439,3201),(2935,3240),(3140,3550),(2545,2357),(2778,2826),(2370,2975)]

def city_dist(a,b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return dist

def rout_lenth(city, rout):
    rout_len = 0
    for i in range(len(rout) - 1):
        rout_len += city_dist(city[rout[i]], city[rout[i+1]])
    rout_len += city_dist(city[rout[len(rout)-1]], city[rout[0]])
    return rout_len

preans = create_preans()
#preans = [21, 0, 31, 48, 34, 33, 35, 38, 39, 37, 36, 47, 23, 4, 14, 5, 3, 24, 45, 43, 15, 49, 19, 22, 17, 16, 2, 44, 18, 40, 7, 8, 9, 42, 32, 50, 11, 27, 26, 25, 46, 12, 13, 51, 10, 28, 29, 1, 6, 41, 20, 30]
#preans = [15, 20, 41, 1, 6, 16, 2, 8, 9, 32, 10, 51, 13, 12, 26, 24, 3, 5, 44, 18, 40, 7, 42, 50, 11, 27, 25, 46, 28, 29, 22, 19, 49, 43, 33, 34, 35, 48, 0, 21, 30, 17, 31, 38, 39, 37, 47, 23, 4, 14, 36, 45]
ans_before = rout_lenth(city,preans)
print("初始解的路径长度：", ans_before)
class LargeNeighborhoodSearch():
    def __init__(self,citys,destory_num, preans):
        self.init_ans = preans
        self.city = citys
        self.part = []
        self.destorynum = destory_num
    #Worst removal heuristic
    def destory(self):
        max_saving = []
        for i in self.init_ans:
            temp = copy.deepcopy(self.init_ans)
            temp.remove(i)
            saving = rout_lenth(self.city, self.init_ans) - rout_lenth(self.city, temp)
            max_saving.append([i,saving])
        max_saving = sorted(max_saving, key=itemgetter(1), reverse=True)
        #print(max_saving)
        for i in range(self.destorynum):
            self.part.append(max_saving[i][0])
            self.init_ans.remove(max_saving[i][0])

    def repair(self):
        for i in self.part:
            temp = copy.deepcopy(self.init_ans)
            min_increse = []
            for j in range(len(temp)):
                temp.insert(j,i)
                increse = rout_lenth(self.city, temp) - rout_lenth(self.city, self.init_ans)
                min_increse.append([j,increse])
                temp.remove(i)
            min_increse = sorted(min_increse, key=itemgetter(1))
            self.init_ans.insert(min_increse[0][0], i)

lns0 = LargeNeighborhoodSearch(city, 10, preans)
lns0.destory()
lns0.repair()
now_ans = lns0.init_ans
if __name__ == '__main__':
    iteration = 100
    for i in range(iteration):
        new_obj = LargeNeighborhoodSearch(city, 10, now_ans)
        new_obj.destory()
        new_obj.repair()
        now_ans = new_obj.init_ans
        print("now dist:",rout_lenth(city, now_ans))
    ans_after = rout_lenth(city, now_ans)
    print("通过大邻域搜索优化后的路径长度：", ans_after)
    print("优化长度：", ans_before - ans_after, "  优化效率：", (ans_before - ans_after)*100/ans_after, "%")
