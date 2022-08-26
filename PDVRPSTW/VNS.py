from objective_func import calculate_cost
import random
import copy
from operator import itemgetter, attrgetter
from read_file import customers_info
from Vhicles import Vehicle
customers = customers_info()
#计算两点距离
def distance(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dist

#计算路径长度
def rout_lenth(rout):
    total = 0
    for i in range(len(rout)-1):
        total += distance(customers[rout[i]], customers[rout[i+1]])
    total += distance(customers[rout[len(rout)-1]], customers[rout[0]])
    return total

class VNS():
    def __init__(self, solution):
        self.solution = solution
        self.destroy_part = []
        #self.random_destroy_part = []
    # def greedy(self):
    #     temp = copy.deepcopy(self.solution)
    #     a = [0]
    #     while len(temp)>0:
    #         min = distance()
    #         for i in range(len(temp)):



    #shaking of 2opt
    def move_of_2opt(self, solution):
        p1, p2 = random.sample(range(len(solution)), 2)
        if p1 > p2:
            p1, p2 = p2, p1
        cut = solution[p1:p2]
        for i in cut:
            if i in solution:
                solution.remove(i)
        for i in range(len(cut)):
            solution.insert(p1, cut[i])

    """******neighborhood structure*******"""
    #2-opt
    def two_opt(self):
        iteration = 1000
        for i in range(iteration):
            cost1 = calculate_cost(self.solution)
            temp = copy.deepcopy(self.solution)
            self.move_of_2opt(temp)
            cost2 = calculate_cost(temp)
            if cost2 < cost1:
                for i in range(len(self.solution)):
                    self.solution[i] = temp[i]
    #
    def move_of_3opt(self, solution):
        a = random.randint(0,len(solution)-6)
        b = a+1
        c = random.randint(b+1, len(solution)-4)
        d = c+1
        e = random.randint(d+1, len(solution)-2)
        f = e+1
        d0 = distance(customers[solution[a]], customers[solution[b]]) + distance(customers[solution[c]], customers[solution[d]]) + distance(customers[solution[e]], customers[solution[f]])
        d1 = distance(customers[solution[a]], customers[solution[c]]) + distance(customers[solution[b]], customers[solution[d]]) + distance(customers[solution[e]], customers[solution[f]])
        d2 = distance(customers[solution[a]], customers[solution[b]]) + distance(customers[solution[c]], customers[solution[e]]) + distance(customers[solution[d]], customers[solution[f]])
        d3 = distance(customers[solution[a]], customers[solution[d]]) + distance(customers[solution[e]], customers[solution[b]]) + distance(customers[solution[c]], customers[solution[f]])
        d4 = distance(customers[solution[f]], customers[solution[b]]) + distance(customers[solution[c]], customers[solution[d]]) + distance(customers[solution[e]], customers[solution[a]])
        if d0 > d1:
            solution[b:d] = reversed(solution[b:d])
            #return d1-d0
        elif d0 > d2:
            solution[d:f] = reversed(solution[d:f])
            #return d2-d0
        elif d0 > d4:
            solution[b:f] = reversed(solution[b:f])
            #return d4-d0
        elif d0 > d3:
            temp = solution[d:f] + solution[b:d]
            solution[b:f] = temp
            #return d3-d0
        #return 0

    def three_opt(self):
        iteration = 1000
        for i in range(iteration):
            self.move_of_3opt(self.solution)
    #local_search
    def local_search(self):
        iteration = 2000
        for i in range(iteration):
            cost1 = calculate_cost(self.solution)
            p1, p2 = random.sample(range(len(self.solution)), 2)
            self.solution[p1], self.solution[p2] = self.solution[p2], self.solution[p1]
            cost2 = calculate_cost(self.solution)
            if cost2 > cost1:
                self.solution[p1], self.solution[p2] = self.solution[p2], self.solution[p1]


    def random_destroy(self, solution):
        p1, p2, p3 = random.sample(solution, 3)
        self.destroy_part.append(p1)
        self.destroy_part.append(p2)
        self.destroy_part.append(p3)
        solution.remove(p1)
        solution.remove(p2)
        solution.remove(p3)

    def random_repair(self, solution):
        for i in self.destroy_part:
            j= random.randint(0, len(solution)-1)
            solution.insert(j, i)

    def worst_destroy(self,solution):
        max_saving = []
        for i in solution:
            temp = copy.deepcopy(solution)
            temp.remove(i)
            saving = calculate_cost(solution) - calculate_cost(temp)
            max_saving.append([i, saving])
        max_saving = sorted(max_saving, key=itemgetter(1), reverse=True)
        for i in range(3):
            self.destroy_part.append(max_saving[i][0])
            solution.remove(max_saving[i][0])

    def best_repair(self, solution):
        for i in self.destroy_part:
            temp = copy.deepcopy(solution)
            min_increase = []
            for j in range(len(temp)):
                temp.insert(j,i)
                increase = calculate_cost(temp) - calculate_cost(solution)
                min_increase.append([j, increase])
                temp.remove(i)
            min_increase = sorted(min_increase, key=itemgetter(1))
            solution.insert(min_increase[0][0], i)
        self.destroy_part.clear()

    #neighborhood structure
    def LNS_random(self):
        iteration = 500
        for i in range(iteration):
            temp = copy.deepcopy(self.solution)
            cost1 = calculate_cost(temp)
            self.random_destroy(temp)
            self.random_repair(temp)
            cost2 = calculate_cost(temp)
            if cost2 < cost1:
                for i in range(len(temp)):
                    self.solution[i] = temp[i]
        self.destroy_part.clear()

    def LNS_greedy(self):
        iteration = 5
        for i in range(iteration):
            temp = copy.deepcopy(self.solution)
            cost1 = calculate_cost(temp)
            self.worst_destroy(temp)
            self.best_repair(temp)
            cost2 = calculate_cost(temp)
            if cost2 < cost1:
                for i in range(len(temp)):
                    self.solution[i] = temp[i]
        self.destroy_part.clear()

    def best_opt(self):
        for i in range(10):
            for i in range(len(self.solution)):
                value = calculate_cost(self.solution)
                D = []
                for j in range(i, len(self.solution)):
                    self.solution[i], self.solution[j] = self.solution[j], self.solution[i]
                    delta = value - calculate_cost(self.solution)
                    D.append([j, delta])
                    self.solution[i], self.solution[j] = self.solution[j], self.solution[i]
                D = sorted(D, key=itemgetter(1), reverse=True)
                self.solution[i], self.solution[D[0][0]] = self.solution[D[0][0]], self.solution[i]

    # def shake(self):
