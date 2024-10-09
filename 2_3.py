# import math
# import random
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Constant
# h = 100
# v0 = 50
# g = 9.81
#
#
# def range(angle):
#     rad_angle = math.radians(angle)
#     t = (v0 * math.sin(rad_angle) + math.sqrt((v0 * math.sin(rad_angle)) ** 2 + 2 * g * h)) / g
#     distance = v0 * math.cos(rad_angle) * t
#     return distance, t
#
#
# def objective_hit(objective_position, projectile_land_position):
#     if objective_position - 5 <= projectile_land_position <= objective_position + 5:
#         print("Objective destoyed!")
#         return True
#     else:
#         print("You missed!")
#         return False
#
#
# def plot_trajectory(angle, flight_time):
#     rad_angle = math.radians(angle)
#
#     t_values = np.linspace(0, flight_time, 500)
#
#     x_values = v0 * np.cos(rad_angle) * t_values
#     y_values = h + v0 * np.sin(rad_angle) * t_values - 0.5 * g * t_values ** 2
#
#     plt.plot(x_values, y_values, color='blue')
#     plt.title("Trajectory of the projectile Warwolf")
#     plt.xlabel("Distance (m)")
#     plt.ylabel("Height (m)")
#     plt.grid(True)
#     plt.savefig("trajectory.png")
#     plt.show()
#
# def trebuchet_simulation():
#     objective = random.randint(50, 340)
#     print(f"Objective is in {objective} meters.")
#
#     attempts = 0
#     hit = False
#     while not hit:
#         attempts += 1
#         alpha_given_by_user = float(input("Please input alpha in (deg.): "))
#         landing_distance, flight_time = range(alpha_given_by_user)
#         print(f"Your projectile landed on distance {round(landing_distance, 2)} meters.")
#         hit = objective_hit(objective, landing_distance)
#
#     print(f"Congratulations! You destroyed the objective in {attempts} attempts.")
#     plot_trajectory(alpha_given_by_user, flight_time)
#
#
# trebuchet_simulation()
