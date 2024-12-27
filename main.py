from deap import base, creator, tools, algorithms
import random
import numpy as np
import matplotlib.pyplot as plt
from model_and_fitness_functions import fitness_ISE, fitness_IAE, fitness_MSE, fitness_ITAE, fitness_ITAE_settling, \
    fitness_multi_objective, create_system, pid_controller, closed_loop_response

# Ustawienie ziarna dla losowości, aby ułatwić porównanie z różnymi parametrami w każdym wywołaniu
SEED = 298837
random.seed(SEED)
np.random.seed(SEED)

# Tworzenie systemu
system = create_system()

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0.01, 10)  # Zakres dla Kp, Ki, Kd
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Rejestracja operatorów genetycznych
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)


# Funkcja oceny (fitness)
def evaluate(individual):
    Kp, Ki, Kd = individual
    fitness_function = toolbox.fitness_function  # Uzyskanie funkcji fitness z toolbox
    fitness_value = fitness_function(Kp, Ki, Kd, system)  # Przekazanie do funkcji fitness
    individual.fitness.values = (fitness_value,)  # Przypisujemy do atrybutu 'values'
    return individual.fitness.values  # Funkcja powinna zwrócić wartości fitness


toolbox.register("evaluate", evaluate)

# Parametry algorytmu genetycznego
population = toolbox.population(n=50)
generations = 20


# Algorytm genetyczny z wyświetlaniem najlepszych parametrów po każdej generacji
def print_best_parameters(population):
    best_individual = tools.selBest(population, k=1)[0]
    Kp, Ki, Kd = best_individual
    print(f"Najlepsze parametry PID w tej generacji: Kp={Kp}, Ki={Ki}, Kd={Kd}")

# Funkcja do optymalizacji na podstawie wybranej funkcji fitness
def optimize(fitness_function, fitness_name):
    # Wyświetlanie informacji o aktualnej funkcji fitness
    print(f"\n=== Rozpoczynanie optymalizacji dla funkcji fitness: {fitness_name} ===\n")

    # Zarejestruj odpowiednią funkcję fitness w toolbox
    toolbox.fitness_function = fitness_function

    for gen in range(generations):
        print(f"Generacja {gen + 1} dla funkcji fitness: {fitness_name}")
        result = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=1,
                                     stats=None, verbose=False)
        # Po zakończeniu generacji wyświetlamy najlepsze parametry PID
        best_individual = tools.selBest(population, k=1)[0]
        Kp, Ki, Kd = best_individual
        print(f"Najlepsze parametry PID w tej generacji: Kp={Kp:.4f}, Ki={Ki:.4f}, Kd={Kd:.4f}")

    # Najlepsze rozwiązanie po wszystkich generacjach
    best_individual = tools.selBest(population, k=1)[0]
    print(f"\n=== Najlepsze parametry PID dla funkcji {fitness_name}: Kp={best_individual[0]:.4f}, "
          f"Ki={best_individual[1]:.4f}, Kd={best_individual[2]:.4f} ===\n")

    return best_individual


# Najlepsze rozwiązanie po wszystkich generacjach
best_individual = tools.selBest(population, k=1)[0]
print(
    f"Najlepsze parametry PID po {generations} generacjach: Kp={best_individual[0]}, Ki={best_individual[1]}, Kd={best_individual[2]}")


# Funkcja rysująca odpowiedź skokową dla najlepszych parametrów regulatora PID
def plot_step_response(system, Kp, Ki, Kd, label, ax):
    # Tworzenie regulatora PID
    pid = pid_controller(Kp, Ki, Kd)
    # Symulacja odpowiedzi skokowej układu zamkniętego
    t, y = closed_loop_response(system, pid)
    # Rysowanie wykresu na odpowiedniej osi (sub-wykresie)
    ax.plot(t, y, label=label)  # Użyj label
    # Dodanie linii wartości zadanej do sub-wykresu
    ax.axhline(1, color="r", linestyle="--", label="Wartość zadana")
    ax.set_xlabel("Czas [s]")
    ax.set_ylabel("Odpowiedź")
    ax.set_title(f"Odpowiedź skokowa dla {label}")
    ax.grid()
    ax.legend()

def compare_fitness_functions():
    fitness_functions = [fitness_ISE, fitness_IAE, fitness_MSE, fitness_ITAE, fitness_ITAE_settling,
                         fitness_multi_objective]
    labels = ['ISE', 'IAE', 'MSE', 'ITAE', 'ITAE_settling', 'multi_objective']

    # Utworzenie sub-wykresów (np. 2 wiersze, 3 kolumny)
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()  # Spłaszczenie tablicy osi do jednego wymiaru

    # Zmienna do przechowywania najlepszych parametrów PID
    best_individuals = {}

    # Optymalizacja dla każdej funkcji fitness i zapisanie najlepszych parametrów
    for i, (fitness_function, label) in enumerate(zip(fitness_functions, labels)):
        best_individuals[label] = optimize(fitness_function, label)  # Przekazujemy nazwę funkcji fitness
        Kp, Ki, Kd = best_individuals[label]
        plot_step_response(system, Kp, Ki, Kd, label, axes[i])

    # Rysowanie wspólnego wykresu dla wszystkich funkcji fitness
    fig_comparison, ax_comparison = plt.subplots(figsize=(10, 6))
    for fitness_function, label in zip(fitness_functions, labels):
        Kp, Ki, Kd = best_individuals[label]  # Używamy wyników zapisanych wcześniej
        pid = pid_controller(Kp, Ki, Kd)
        t, y = closed_loop_response(system, pid)
        ax_comparison.plot(t, y, label=label)

    # Dodanie wartości zadanej na wspólnym wykresie
    ax_comparison.axhline(1, color="r", linestyle="--", label="Wartość zadana")

    # Ustawienia wspólnego wykresu
    ax_comparison.set_xlabel("Czas [s]")
    ax_comparison.set_ylabel("Odpowiedź")
    ax_comparison.set_title("Porównanie odpowiedzi skokowych dla różnych funkcji fitness")
    ax_comparison.legend()
    ax_comparison.grid()

    # Dopasowanie układu sub-wykresów
    plt.tight_layout()
    plt.show()


# Symulacja i wizualizacja dla różnych funkcji fitness
compare_fitness_functions()
