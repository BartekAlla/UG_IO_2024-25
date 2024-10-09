import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Stałe
h = 100  # Wysokość trebusza [m]
v0 = 50  # Początkowa prędkość [m/s]
g = 9.81  # Przyspieszenie ziemskie [m/s^2]

# Funkcja obliczająca zasięg i czas lotu dla danego kąta
def calculate_range(angle_deg):
    angle_rad = math.radians(angle_deg)
    # Czas lotu, obliczony na podstawie równania ruchu
    flight_time = (v0 * math.sin(angle_rad) + math.sqrt((v0 * math.sin(angle_rad)) ** 2 + 2 * g * h)) / g
    # Zasięg (dystans w poziomie)
    distance = v0 * math.cos(angle_rad) * flight_time
    return distance, flight_time

# Funkcja sprawdzająca, czy pocisk trafił w cel
def objective_hit(objective_position, projectile_land_position, margin=5):
    return objective_position - margin <= projectile_land_position <= objective_position + margin

# Funkcja rysująca trajektorię pocisku
def plot_trajectory(angle_deg, flight_time):
    angle_rad = math.radians(angle_deg)

    # Tworzenie wartości czasowych od 0 do czasu lotu
    t_values = np.linspace(0, flight_time, 500)

    # Obliczenie pozycji x i y w każdym momencie czasu
    x_values = v0 * np.cos(angle_rad) * t_values
    y_values = h + v0 * np.sin(angle_rad) * t_values - 0.5 * g * t_values ** 2

    # Rysowanie trajektorii
    plt.plot(x_values, y_values, color='blue')
    plt.title("Trajectory of the projectile Warwolf")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)

    # Zapis wykresu do pliku PNG
    plt.savefig("trajectory.png")
    plt.show()

# Główna funkcja symulacji trebusza
def trebuchet_simulation():
    # Losowanie odległości celu
    objective = random.randint(50, 340)
    print(f"Objective is located {objective} meters away.")

    attempts = 0
    hit = False

    # Pętla, dopóki nie trafi w cel
    while not hit:
        attempts += 1

        # Użytkownik podaje kąt strzału
        alpha_given_by_user = float(input("Please input alpha in degrees: "))

        # Obliczanie zasięgu i czasu lotu pocisku
        landing_distance, flight_time = calculate_range(alpha_given_by_user)
        print(f"Your projectile landed at {round(landing_distance, 2)} meters.")

        # Sprawdzenie, czy pocisk trafił w cel
        hit = objective_hit(objective, landing_distance)

        if hit:
            print(f"Congratulations! You destroyed the objective in {attempts} attempts.")
        else:
            print("You missed! Try again.")

    # Rysowanie i zapisywanie trajektorii pocisku
    plot_trajectory(alpha_given_by_user, flight_time)

# Uruchomienie symulacji
trebuchet_simulation()
# 1. Usprawnienia zaproponowane przez AI poprawiły czytelność programu poprzez zmiane nazwy niektórych funkcji i zmiennych
# np. range() -> calculate_range(), zmienne w funkcji calculate_range() z d, t -> distance, flight time.
# 2. Dodatkowym aspektem jest rozdzielenie funkcji logicznych od wyświetlanych komunikatów np. funkcja objective_hit()
# nie wyświetla juz tekstu, a jedynie zwraca wynik logiczny, natomiast samo wyświetlanie tekstu zostało przeniesione
# do funkcji trebuchet_simulation(). Dodaje to modularności do programu przez co funkcja ta może zostać wykorzystana
# w innym celu.
# 3. Wprowadzono dodatkową parametryzację funkcji (objective_hit()), przez co w przypadku zmiany marginesu obliczania
# trafionego celu wystaczy zmienic jedynie parametr, zamiast modyfikować całą funkcję.
# Podsumowanie: Zaproponowane usprawnienia przez AI powodują, że program jest czytelniejszy, bardziej modularny oraz
# bardziej elastyczny.