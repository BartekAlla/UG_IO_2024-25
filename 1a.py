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

print("It's your " + str(days_of_life(date_of_birth, current_date)) + " day of life!")

def physical_wave(age_in_days):
    return math.sin((2 * math.pi * age_in_days) / 23)


def emotional_wave(age_in_days):
    return math.sin((2 * math.pi * age_in_days) / 28)


def intellectual_wave(age_in_days):
    return math.sin((2 * math.pi * age_in_days) / 33)


print(name)
print(date_of_birth)
print(current_date)
print(days_of_life(date_of_birth, current_date))
print(physical_wave(days_of_life(date_of_birth, current_date)))
print(emotional_wave(days_of_life(date_of_birth, current_date)))
print(intellectual_wave(days_of_life(date_of_birth, current_date)))
