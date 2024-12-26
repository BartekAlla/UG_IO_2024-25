from deap import base, creator, tools, algorithms
import random
import matplotlib.pyplot as plt
from model_and_fitness_functions import fitness_ISE, fitness_IAE, fitness_MSE, fitness_ITAE, fitness_ITAE_settling, fitness_multi_objective, create_system, pid_controller, closed_loop_response

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
    # Obliczamy błąd ISE
    ise_value = fitness_ISE(Kp, Ki, Kd, system)
    individual.fitness.values = (ise_value,)  # Przypisujemy do atrybutu 'values'
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


# Algorytm genetyczny
for gen in range(generations):
    print(f"Generacja {gen + 1}")
    result = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=1,
                                 stats=None, verbose=False)
    # Po zakończeniu generacji, wyświetlamy najlepsze parametry PID
    print_best_parameters(population)

# Najlepsze rozwiązanie po wszystkich generacjach
best_individual = tools.selBest(population, k=1)[0]
print(
    f"Najlepsze parametry PID po {generations} generacjach: Kp={best_individual[0]}, Ki={best_individual[1]}, Kd={best_individual[2]}")


# Funkcja rysująca odpowiedź skokową dla najlepszych parametrów regulatora PID
def plot_step_response(system, Kp, Ki, Kd):
    # Tworzenie regulatora PID
    pid = pid_controller(Kp, Ki, Kd)

    # Symulacja odpowiedzi skokowej układu zamkniętego
    t, y = closed_loop_response(system, pid)

    # Rysowanie wykresu
    plt.plot(t, y, label="Odpowiedź układu")
    plt.axhline(1, color="r", linestyle="--", label="Wartość zadana")
    plt.xlabel("Czas [s]")
    plt.ylabel("Wyjście")
    plt.title("Odpowiedź skokowa układu z optymalnym PID")
    plt.legend()
    plt.grid()
    plt.show()


# Symulacja i wizualizacja dla najlepszych parametrów
Kp, Ki, Kd = best_individual  # Parametry PID
plot_step_response(system, Kp, Ki, Kd)
