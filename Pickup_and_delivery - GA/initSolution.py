import random
import copy
from read_file import customers_info

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

#车辆类
class Vehicle():
    def __init__(self):
        self.startcost = 500
        self.load = 150
        self.cost_per_km = 5
        self.speed = 50
        self.rout = [0]
        self.totalcost = 0

    #计算一条路径的成本
    def calculate_cost(self):
        #travel cost
        travel_cost = self.cost_per_km * rout_lenth(self.rout)


        self.totaldist = rout_lenth(self.rout)
        #calculate total cost
        self.totalcost = self.startcost + travel_cost
        self.travel_cost = travel_cost

class Population():
    def __init__(self, S, nodes_num):
        self.S = S
        self.nodes_num = nodes_num

    def init_indi(self):
        individual = list(range(2, self.nodes_num + 2))
        random.shuffle(individual)
        return individual

    def init_pop(self):
        self.pop = []
        for i in range(self.S):
            self.pop.append(self.init_indi())

def calculate_fitness_withPD(individual):
    vehicles = []
    temp = copy.deepcopy(individual)
    while len(temp) > 0:
        now_take = 0
        temp_rout = []
        v = Vehicle()
        for i in temp:
            if customers[i][2] + now_take <= v.load:
                now_take += customers[i][2]
                temp_rout.append(i)
            else:
                break
        for j in temp_rout:
            if now_take - customers[j][2] + customers[j][3] <= v.load:
                v.rout.append(j)
                now_take = now_take - customers[j][2] + customers[j][3]
        v.rout.append(1)
        v.rout.append(0)
        vehicles.append(v)
        for i in v.rout:
            if i in temp:
                temp.remove(i)
    cost = 0
    for vehicle in vehicles:
        vehicle.calculate_cost()
        cost += vehicle.totalcost
    fit = 1/cost
    return fit


def calculate_fitness_withP(individual):
    vehicles = []
    temp = copy.deepcopy(individual)
    while len(temp) > 0:
        now_take = 0 #
        v = Vehicle()
        for i in temp:
            if customers[i][2] + now_take <= v.load:
                now_take += customers[i][2]
                v.rout.append(i)
            else:
                break
        v.rout.append(0)
        vehicles.append(v)
        for i in v.rout:
            if i in temp:
                temp.remove(i)
    cost = 0
    for i in vehicles:
        i.calculate_cost()
        cost += i.totalcost
    fit = 1 / cost
    return fit

def calculate_fitness_withD(individual):
    vehicles = []
    temp = copy.deepcopy(individual)
    while len(temp) > 0:
        now_take = 0
        v = Vehicle()
        for i in temp:
            if customers[i][2] + now_take <= v.load:
                now_take += customers[i][3]
                v.rout.append(i)
            else:
                break
        #v.rout.append(1)
        v.rout.append(0)
        vehicles.append(v)
        for i in v.rout:
            if i in temp:
                temp.remove(i)
    cost = 0
    for i in vehicles:
        i.calculate_cost()
        cost += i.totalcost
    fit = 1 / cost
    return fit

def pop_fitness_PD(pop):
    population = []
    for i in range(len(pop)):
        fit = calculate_fitness_withPD(pop[i])
        population.append(fit)
    return population

def pop_fitness_withP(pop):
    population = []
    for i in range(len(pop)):
        fit = calculate_fitness_withP(pop[i])
        population.append(fit)
    return population

def pop_fitness_withD(pop):
    population = []
    for i in range(len(pop)):
        fit = calculate_fitness_withD(pop[i])
        population.append(fit)
    return population

