import datetime
import math

name = input("What's your name? ")
year_of_birth = input("What's your year of birth? ")
month_of_birth = input("What's your month of birth? ")
day_of_birth = input("What's your day of birth? ")
print("Hello " + name + "!")

date_of_birth = datetime.date(int(year_of_birth), int(month_of_birth), int(day_of_birth))
current_date = datetime.date.today()


def days_of_life(date_of_birth, current_date):
    return (current_date - date_of_birth).days


def physical_wave(age_in_days):
    return math.sin((2 * math.pi * age_in_days) / 23)


def emotional_wave(age_in_days):
    return math.sin((2 * math.pi * age_in_days) / 28)


def intellectual_wave(age_in_days):
    return math.sin((2 * math.pi * age_in_days) / 33)


print("Your date of birth is: " + year_of_birth + "-" + month_of_birth + "-" + day_of_birth)
print("Today is: " + str(current_date.year) + "-" + str(current_date.month) + "-" + str(current_date.day))
print("It's your " + str(days_of_life(date_of_birth, current_date)) + " day of life!")
print("Your physical wave for today is: " + str(physical_wave(days_of_life(date_of_birth, current_date))))
print("Your emotional wave for today is: " + str(emotional_wave(days_of_life(date_of_birth, current_date))))
print("Your intellectual wave for today is: " + str(intellectual_wave(days_of_life(date_of_birth, current_date))))
