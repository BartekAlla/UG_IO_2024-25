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
# def trebuchet_simulation():
#     objective = random.randint(50, 340)
#     print(f"Objective is in {objective} meters.")
#
#     alpha_given_by_user = float(input("Please input alpha in (deg.): "))
#
#     landing_distance = range(alpha_given_by_user)
#     print(f"Your projectile landed on distance {round(landing_distance, 2)} meters.")
#
#     if objective - 5 <= landing_distance <= objective + 5:
#         print("Objective destoyed!")
#     else:
#         print("You missed!")
#
#
# trebuchet_simulation()
