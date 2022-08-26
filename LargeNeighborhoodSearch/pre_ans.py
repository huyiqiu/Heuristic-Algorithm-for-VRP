"""用贪心+禁忌搜索产生初始解"""
import numpy as np
import matplotlib.pyplot as plt
import random
import copy
#柏林
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

tabulenth = 10
class TabuSearch():
    def __init__(self, citys, iteration):
        self.citys = citys
        self.city_num = len(citys)
        self.tabu_list = [] #禁忌表
        self.ans = list(range(len(citys))) #初始化一个解
        self.bsf = copy.deepcopy(self.ans) #best so far
        self.iteration = iteration
        self.trend = [] #每次迭代的最优解数值

    def init_ans(self):
        ans = []
        for i in range(len(self.citys)):
            min = 100000
            new = 0
            if i == 0:
                ans.append(0)
                continue
            else:
                for j in self.ans:
                    if city_dist(self.citys[ans[i-1]], self.citys[j]) < min and j not in ans:
                        min = city_dist(self.citys[ans[i-1]], self.citys[j])
                        new = j
                ans.append(new)
        self.ans = copy.deepcopy(ans)


    def create_new(self):

        """1.设置候选解列表，长度为500
           2.记录每次交换的Δ = 交换前目标函数值 - 交换后目标函数值  Δ越大表面交换效果越好
           3.在500个候选解中选择最好的那次交换，同时将其加入禁忌表"""

        if len(self.tabu_list) == tabulenth: #检查禁忌表是否满，已满则删除最早进表的交换操作
            self.tabu_list.pop()
        delta = []
        tabu = []
        for i in range(500):
            a1, a2 = random.sample(list(range(self.city_num)), 2)
            if a1 > a2:
                a1, a2 = a2, a1
            if [a1, a2] in self.tabu_list:
                continue
            lenth_before = rout_lenth(self.citys, self.ans)
            self.ans[a1], self.ans[a2] = self.ans[a2], self.ans[a1]
            delta.append(lenth_before - rout_lenth(self.citys, self.ans))
            tabu.append([a1, a2])
            self.ans[a1], self.ans[a2] = self.ans[a2], self.ans[a1]
        this_best = tabu[delta.index(max(delta))]
        self.ans[this_best[0]], self.ans[this_best[1]] = self.ans[this_best[1]], self.ans[this_best[0]]
        self.tabu_list.insert(0, this_best)

        if rout_lenth(self.citys, self.ans) < rout_lenth(self.citys, self.bsf):
            for i in range(len(self.bsf)):
                self.bsf[i] = self.ans[i]

    def tabu_process(self):
        for i in range(self.iteration):
            self.create_new()
            print("当前禁忌表：", self.tabu_list)
            nowbest = rout_lenth(self.citys, self.bsf)
            print("当前最优解:", nowbest)
            self.trend.append(nowbest)
    def draw_trend(self):
        plt.plot(self.trend)
        plt.show()

    def draw(self):
        for i in range(len(self.ans) - 1):
            a = (self.citys[self.ans[i]][0], self.citys[self.ans[i + 1]][0])
            b = (self.citys[self.ans[i]][1], self.citys[self.ans[i + 1]][1])
            plt.plot(a, b, '.-', color='#87CEEB')
        a = (self.citys[self.ans[len(self.ans) - 1]][0], self.citys[self.ans[0]][0])
        b = (self.citys[self.ans[len(self.ans) - 1]][1], self.citys[self.ans[0]][1])
        plt.plot(a, b, '.-', color='#87CEEB')
        plt.show()
def create_preans():
    pre_ans = TabuSearch(city, 200)
    pre_ans.init_ans()
    pre_ans.tabu_process()
    print("the route is:", pre_ans.bsf, "which answer is ", rout_lenth(city, pre_ans.bsf))
    pre_ans.draw()
    return pre_ans.bsf

create_preans()

