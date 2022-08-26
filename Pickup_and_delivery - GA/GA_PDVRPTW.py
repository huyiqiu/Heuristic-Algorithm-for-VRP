from initSolution import Population
import random
import copy
from read_file import customers_info
from GAoperator import GAoperators
import numpy as np
customers = customers_info()
min_init = 100000



def GA():
    iteration = 1000
    pop = Population(100, len(customers) - 2)
    pop.init_pop()
    population = pop.pop
    GA_PD = GAoperators(1, population, 0.8, 0.05)
    best_ever = []
    mincost = min_init
    for i in range(iteration):
        GA_PD.fit()
        GA_PD.choose()
        GA_PD.exchange()
        GA_PD.mutation()
        #GA_PD.LS()
        nowbest, nowcost = GA_PD.find_best()
        if nowcost < mincost:
            best_ever = copy.deepcopy(nowbest)
            mincost = nowcost
        print("第",i,"次迭代")
        print("当前最优个体：",nowbest,"最优个体：", best_ever)
        print(nowcost, mincost)
    GA_PD.LS()
    return best_ever, mincost


# for i in range(10):
#     rout, cost = GA()
#     print(rout, cost)
def run_10times():
    answers = []
    routes = []
    for i in range(10):
        rout, cost = GA()
        answers.append(cost)
        routes.append(rout)
    avg = np.mean(answers)
    std = np.std(answers, ddof=1)
    for i in range(10):
        print(answers[i],":",routes[i])
    print("the average:", avg, "\nthe std:", std)

run_10times()



