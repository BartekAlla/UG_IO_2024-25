import pygad
import math


def endurance(x, y, z, u, v, w):
    return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)


def fitness_function(ga_instance, solution, solution_idx):
    x, y, z, u, v, w = solution
    return endurance(x, y, z, u, v, w)


gene_space = {'low': 0.0, 'high': 1.0}
sol_per_pop = 10
num_genes = 6
num_parents_mating = 5
num_generations = 30
keep_parents = 2
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 15

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()

print("Najlepsze rozwiązanie (chromosom):", solution)
print("Wytrzymałość dla najlepszego rozwiązania:", solution_fitness)
ga_instance.plot_fitness()

for _ in range(5):
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Najlepsze rozwiązanie (chromosom):", solution)
    print("Wytrzymałość dla najlepszego rozwiązania:", solution_fitness)
    ga_instance.plot_fitness()
# Najlepsze rozwiązanie (chromosom): [0.24864232 0.24583298 0.99591658 0.9991594  0.12720317 0.00230868]
# Wytrzymałość dla najlepszego rozwiązania: 2.8388020305952693
# Wyniki oraz wykresy się zmieniają jednak w przybliżeniu wszystkie są w okolicy 2.82
