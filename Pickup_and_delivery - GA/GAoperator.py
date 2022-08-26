import random
import copy
from read_file import customers_info
from initSolution import Population, pop_fitness_PD, pop_fitness_withP, pop_fitness_withD, calculate_fitness_withP, calculate_fitness_withPD, calculate_fitness_withD

def fit_func(problem, indi):
    if problem == 1:
        f = calculate_fitness_withPD(indi)
    elif problem == 2:
        f = calculate_fitness_withP(indi)
    else:
        f = calculate_fitness_withD(indi)
    return f

class GAoperators():
    def __init__(self, problem, pop, pc, pm):
        self.problem = problem
        self.pop = pop
        self.n = len(pop)
        self.pc = pc
        self.pm = pm


    def fit(self):
        if self.problem == 1:
            self.fitness = pop_fitness_PD(self.pop)
        elif self.problem == 2:
            self.fitness = pop_fitness_withP(self.pop)
        elif self.problem == 3:
            self.fitness = pop_fitness_withD(self.pop)

    def choose(self):
        self.fit()
        fit_sum = sum(self.fitness)
        prob = []
        for i in self.fitness:
            prob.append(i/fit_sum)
        #print(len(prob))
        prob_distribution = []
        prob_distribution.append(prob[0])
        for i in range(1, self.n):
            prob_distribution.append(prob[i] + prob_distribution[i-1])
        new_pop = []
        new_pop.append(self.pop[self.fitness.index(max(self.fitness))])
        for i in range(self.n - 1):
            rand = random.uniform(0, 1)
            if rand < prob_distribution[0]:
                temp = copy.deepcopy(self.pop[0])
                new_pop.append(temp)
            for j in range(1, self.n):
                if rand < prob_distribution[j] and rand > prob_distribution[j-1]:
                    temp = copy.deepcopy(self.pop[j])
                    new_pop.append(temp)
        self.pop.clear()
        for i in range(self.n):
            self.pop.append(new_pop[i])

    def exchange_move(self, a, b):
        p1, p2 = random.sample(range(len(a)), 2)
        if p1 > p2:
            p1, p2 = p2, p1
        cuta, cutb = a[p1:p2], b[p1:p2]
        tempa, tempb = copy.deepcopy(a), copy.deepcopy(b)
        for i in tempa:
            if i in cutb:
                a.remove(i)
        for i in cutb:
            a.append(i)
        for i in tempb:
            if i in cuta:
                b.remove(i)
        for i in range(len(cuta)):
            b.insert(0, cuta[len(cuta) - i - 1])

    def exchange(self):
        self.fit()
        best = copy.deepcopy(self.pop[self.fitness.index(max(self.fitness))])
        for i in range(int(self.n / 2)):
            rand = random.uniform(0, 1)
            if rand < self.pc:
                self.exchange_move(self.pop[i * 2], self.pop[i * 2 + 1])
        self.pop.remove(self.pop[self.fitness.index(min(self.fitness))])
        self.pop.append(best)

    def mutation(self):
        self.fit()
        best = copy.deepcopy(self.pop[self.fitness.index(max(self.fitness))])
        for i in range(self.n):
            rand = random.uniform(0, 1)
            if rand < self.pm:
                p1, p2 = random.sample(range(15), 2) ##############
                self.pop[i][p1], self.pop[i][p2] = self.pop[i][p2], self.pop[i][p1]
        self.pop.remove(self.pop[self.fitness.index(min(self.fitness))])
        self.pop.append(best)
    #局部优化
    def LS(self):
        self.fit()
        best = copy.deepcopy(self.pop[self.fitness.index(max(self.fitness))])
        for i in range(len(best)):
            value = 1 / fit_func(self.problem, best)
            bestj = i
            for j in range(i + 1, len(best)):
                best[i], best[j] = best[j], best[i]
                if 1 / fit_func(self.problem, best) > value:
                    bestj = j
                best[i], best[j] = best[j], best[i]
            best[i], best[bestj] = best[bestj], best[i]
        self.pop.remove(self.pop[self.fitness.index(min(self.fitness))])
        self.pop.append(best)

    def find_best(self):
        self.fit()
        best = copy.deepcopy(self.pop[self.fitness.index(max(self.fitness))])
        mincost = 1 / max(self.fitness)
        return best, mincost