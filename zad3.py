import numpy as np
import pygad
import time

# a)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

maze_np = np.array(maze)
for row in maze:
    print(row)

# b)
gene_space = [0, 1, 2, 3]
moves = {
    0: (-1, 0),  # Góra
    1: (1, 0),  # Dół
    2: (0, -1),  # Lewo
    3: (0, 1)  # Prawo
}
# Długość chromosomu jako maks liczba kroków
num_genes = 30

# c)
sol_per_pop = 50
num_parents_mating = 5
num_generations = 100
keep_parents = 2
parent_selection_type = "sss"
crossover_type = "uniform"
mutation_type = "random"
stop_criteria = ["reach_0"]

# d)
mutation_percent_genes = 10


# e)
def fitness_func(ga_instance, solution, solution_idx):
    start = (1, 1)
    exit = (10, 10)
    current_position = list(start)

    for gene in solution:
        move = moves[gene]
        new_position = [
            current_position[0] + move[0],
            current_position[1] + move[1]
        ]
        if maze[new_position[0]][new_position[1]] == 0:
            current_position = new_position

    abs_distance = abs(current_position[0] - exit[0]) + abs(current_position[1] - exit[1])
    return -abs_distance


successful_trials = 0


def on_stop(ga_instance, stop_criteria):
    global successful_trials
    solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
    if solution_fitness == 0:
        successful_trials += 1
        print(f"Osiągnięto kryterium stopu: {solution_fitness}")
        print("Najlepsze rozwiązanie (binarne):", solution)
        ga_instance.plot_fitness()


times = []
while successful_trials < 10:
    start = time.time()
    ga_instance = pygad.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_func,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           stop_criteria=stop_criteria,
                           on_stop=on_stop)
    ga_instance.run()
    end = time.time()
    print(f"Liczba generacji {ga_instance.generations_completed}")
    if np.max(ga_instance.last_generation_fitness) == 0:
        times.append(end - start)

average_time = np.mean(times)
print(f"Średni czas działania algorytmu: {average_time:.4f} sekundy")

# f) Średni czas działania algorytmu: 0.3808 sekundy
