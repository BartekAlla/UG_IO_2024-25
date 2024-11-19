import pygad
import time
import numpy as np

# a)
items = {
    "zegar": (100, 7),
    "obraz-pejzaz": (300, 7),
    "obraz-portret": (200, 6),
    "radio": (40, 2),
    "laptop": (500, 5),
    "lampka nocna": (70, 6),
    "srebrne sztucce": (100, 1),
    "porcelana": (250, 3),
    "figura z brazu": (300, 10),
    "skorzana torebka": (280, 3),
    "odkurzacz": (300, 15)
}


# b)
def fitness_function(ga_instance, solution, solution_idx):
    total_value = 0
    total_weight = 0
    weight_limit = 25
    item_list = list(items.values())

    for i, selected in enumerate(solution):
        if selected == 1:
            total_value += item_list[i][0]
            total_weight += item_list[i][1]

    if total_weight > weight_limit:
        return 0
    return total_value


# c)
gene_space = [0, 1]
sol_per_pop = 10
num_genes = len(items)
num_parents_mating = 5
num_generations = 30
keep_parents = 2
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 10
stop_criteria = ["reach_1630"]
fitness_values = []
successful_trials = 0


def on_generation(ga_instance):
    best_fitness = ga_instance.best_solution()[1]
    fitness_values.append(best_fitness)


def on_stop(ga_instance, stop_criteria):
    global successful_trials
    solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
    if solution_fitness == 1630:
        successful_trials += 1
        print(f"Osiągnięto kryterium stopu: {solution_fitness}")
        print("Najlepsze rozwiązanie (binarne):", solution)
        selected_items = []
        for i in range(len(solution)):
            if solution[i] == 1:
                item_name = list(items.keys())[i]
                selected_items.append(item_name)

        print("Wybrane przedmioty:", selected_items)

        ga_instance.plot_fitness()


times = []

while successful_trials < 10:
    start = time.time()
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
                           mutation_percent_genes=mutation_percent_genes,
                           on_generation=on_generation,
                           stop_criteria=stop_criteria,
                           on_stop=on_stop)
    ga_instance.run()
    end = time.time()
    print(f"Liczba generacji {ga_instance.generations_completed}")
    if np.max(ga_instance.last_generation_fitness) == 1630:
        times.append(end - start)

average_time = np.mean(times)
print(f"Średni czas działania algorytmu: {average_time:.4f} sekundy")

# d)
# Najlepsze rozwiązanie (binarne): [0. 1. 1. 0. 1. 0. 1. 1. 0. 1. 0.]
# Wartość rozwiązania (fitness): 1630
# Wybrane przedmioty: ['obraz-pejzaz', 'obraz-portret', 'laptop', 'srebrne sztucce', 'porcelana', 'skorzana torebka']
# Wartość wybranych przedmiotów: 1630
# e) 80%
# f) 0.2461 sekundy
