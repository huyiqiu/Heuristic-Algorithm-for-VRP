import random
solution = [1,2,3,4,5,6,7,8,9]
destroy_part = []
def random_destroy(solution):
    p1, p2, p3 = random.sample(solution, 3)
    print(p1,p2,p3)
    destroy_part.append(p1)
    destroy_part.append(p2)
    destroy_part.append(p3)
    solution.remove(p1)
    solution.remove(p2)
    solution.remove(p3)
random_destroy(solution)
print(solution)
print(destroy_part)