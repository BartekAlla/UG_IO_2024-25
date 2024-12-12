import matplotlib.pyplot as plt
import random

from aco import AntColony


plt.style.use("dark_background")


COORDS = (
    (20, 52), (43, 50), (20, 84), (70, 65), (29, 90), (87, 83), (73, 23),
    (10, 15), (55, 44), (85, 65), (90, 20), (33, 77), (50, 30), (77, 90)
)


def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()

colony = AntColony(
    COORDS, ant_count=300, alpha=0.5, beta=1.2,
    pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
    iterations=300
)

optimal_nodes = colony.get_path()


for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )


plt.show()

# Dla defaultowych: 355.55909478663426
# Po zmianie liczby mrówek na 500: 410.0291314049857
# Zmniejszenie pheromone_evaporation_rate na 0.3: 425.33906437839494
# Zmiana wpływu eurestyki beta na 2: 425.33906437839494
# Zmiana itercji na 500: 368.2627057188553
# Wszystko razem: 424.7998311547383