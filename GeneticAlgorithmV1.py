#Question#01
#This is genetic algorithm code for one-max optimization,
#GA generates a string of length 50 in whcih all values are 1.
#The best solution [ 1,1,1,1..............1] i.e. 50 1s.
# For example, a bitstring with a length of 20 bits will have a score of 20 for a string of all 1s.
from numpy.random import randint
from numpy.random import rand
import random
from matplotlib import pyplot
def onemax(x):
    return -sum(x)
def selection(pop, scores):
    k=10
    candidates = random.sample(range(len(pop)), k)
    winner = min(candidates, key=lambda x: scores[x])
    return pop[winner]
def crossover(p1, p2, r_cross):
    c1, c2 = p1.copy(), p2.copy()
    if rand() < r_cross:
        pt = randint(1, len(p1)-2)
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]
def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        if rand() < r_mut:
            bitstring[i] = 1 - bitstring[i]
def genetic_algorithm(values,objective, chromosome_size, n_iter, n_pop, r_cross, r_mut):
    pop = [randint(0, 2, chromosome_size).tolist() for _ in range(n_pop)]
    best, best_eval = 0, objective(pop[0])
    for gen in range(n_iter):
        scores = [objective(c) for c in pop]
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
        children = list()
        for i in range(0, n_pop, 2):
            parent1 = selection(pop, scores)
            parent2 = selection(pop, scores)
            p1, p2 = parent1, parent2
            for c in crossover(p1, p2, r_cross):
                mutation(c, r_mut)
                children.append(c)
        pop = children
        values.append(best_eval)
        print("Generation is >%d, Fitness = %.3f" % (gen, scores[i]))
    return [best, best_eval,values]
n_iter = 30
chromosome_size = 50
n_pop = 100
r_cross = 0.9
r_mut = 1.0 / float(chromosome_size)
values=[]
best, score,values = genetic_algorithm(values,onemax, chromosome_size, n_iter, n_pop, r_cross, r_mut)
print('f(%s) = %f' % (best, score))
pyplot.plot(values, '.-')
pyplot.title("Fitness History Generation by Generation")
pyplot.xlabel('Generations/Iterations')
pyplot.ylabel('Fitness')
pyplot.show()