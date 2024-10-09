import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 100  # Height of the trebuchet [m]
v0 = 50  # Initial velocity [m/s]
g = 9.81  # Gravitational acceleration [m/s^2]


# Function calculating the range and flight time for a given angle
def calculate_range(angle_deg):
    angle_rad = math.radians(angle_deg)
    # Flight time, calculated based on motion equations
    flight_time = (v0 * math.sin(angle_rad) + math.sqrt((v0 * math.sin(angle_rad)) ** 2 + 2 * g * h)) / g
    # Range (horizontal distance)
    distance = v0 * math.cos(angle_rad) * flight_time
    return distance, flight_time


# Function checking if the projectile hit the target
def objective_hit(objective_position, projectile_land_position, margin=5):
    return objective_position - margin <= projectile_land_position <= objective_position + margin


# Function plotting the projectile's trajectory
def plot_trajectory(angle_deg, flight_time):
    angle_rad = math.radians(angle_deg)

    # Create time values from 0 to flight time
    t_values = np.linspace(0, flight_time, 500)

    # Calculate x and y positions at each moment in time
    x_values = v0 * np.cos(angle_rad) * t_values
    y_values = h + v0 * np.sin(angle_rad) * t_values - 0.5 * g * t_values ** 2

    # Plotting the trajectory
    plt.plot(x_values, y_values, color='blue')
    plt.title("Trajectory of the projectile Warwolf")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)

    # Save the plot as a PNG file
    plt.savefig("trajectory.png")
    plt.show()


# Main function for trebuchet simulation
def trebuchet_simulation():
    # Randomly select the target distance
    objective = random.randint(50, 340)
    print(f"Objective is located {objective} meters away.")

    attempts = 0
    hit = False

    # Loop until the target is hit
    while not hit:
        attempts += 1

        # User inputs the shooting angle
        alpha_given_by_user = float(input("Please input alpha in degrees: "))

        # Calculate the projectile's range and flight time
        landing_distance, flight_time = calculate_range(alpha_given_by_user)
        print(f"Your projectile landed at {round(landing_distance, 2)} meters.")

        # Check if the projectile hit the target
        hit = objective_hit(objective, landing_distance)

        if hit:
            print(f"Congratulations! You destroyed the objective in {attempts} attempts.")
        else:
            print("You missed! Try again.")

    # Plot and save the projectile's trajectory
    plot_trajectory(alpha_given_by_user, flight_time)


# Run the simulation
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
