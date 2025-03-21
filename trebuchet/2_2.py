# import math
# import random
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
#     return distance
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
# def trebuchet_simulation():
#     objective = random.randint(50, 340)
#     print(f"Objective is in {objective} meters.")
#
#     attempts = 0
#     hit = False
#     while not hit:
#         attempts += 1
#         alpha_given_by_user = float(input("Please input alpha in (deg.): "))
#         landing_distance = range(alpha_given_by_user)
#         print(f"Your projectile landed on distance {round(landing_distance, 2)} meters.")
#         hit = objective_hit(objective, landing_distance)
#
#     print(f"Congratulations! You destroyed the objective in {attempts} attempts.")
#
#
# trebuchet_simulation()
