import random
import numpy as np

p_n = 50
n_dimensions = 30
n_iter = 1000


def population():
    pop = [np.random.choice([0, 1], size=(n_dimensions)) for i in range(p_n)]
    return pop


def fitness(pop):
    pop.sort(key=sort_key, reverse=True)
    return pop


def selection(pop):
    r1 = np.random.randint(0, len(pop) - 1)
    r2 = np.random.randint(0, len(pop) - 1)
    xi = pop[r1]
    xj = pop[r2]
    mates = (xi, xj)
    return mates


def crossover(mates):
    parent1 = mates[0]
    parent2 = mates[1]

    offspring1 = np.zeros(n_dimensions, dtype=np.int)
    offspring2 = np.zeros(n_dimensions, dtype=np.int)

    rnd = np.random.randint(0, n_dimensions)
    offspring1[0: rnd] = parent1[0: rnd]
    offspring1[rnd:n_dimensions] = parent2[rnd:n_dimensions]

    offspring2[0: rnd] = parent2[0: rnd]
    offspring2[rnd:n_dimensions] = parent1[rnd:n_dimensions]

    return offspring1, offspring2


def mutation(pop):
    rnd = np.random.randint(100)
    if rnd < 2:
        rnd = np.random.randint(p_n)
        rnd2 = np.random.randint(n_dimensions)
        tmp = pop[rnd][rnd2]
        if tmp == 0:
            pop[rnd][rnd2] = 1
        else:
            pop[rnd][rnd2] = 0
    return pop


def sort_key(item):
    sum = 0
    for i in item:
        if i == 1:
            sum += 1
    return sum


def main():
    pop = population()
    pop = fitness(pop)
    print(pop[0])
    for i in range(n_iter):
        for i in range(50):
            mates = selection(pop)
            offspring1, offspring2 = crossover(mates)
            if offspring1 is not None:
                pop.append(offspring1)
            if offspring2 is not None:
                pop.append(offspring2)
        pop = mutation(pop)
        pop = fitness(pop)
        pop = pop[0:p_n]
    print(pop[0])

if __name__ == '__main__':
    main()
