import datetime
import math


def get_birth_details():
    name = input("What's your name? ")
    year_of_birth = int(input("What's your year of birth? "))
    month_of_birth = int(input("What's your month of birth? "))
    day_of_birth = int(input("What's your day of birth? "))

    date_of_birth = datetime.date(year_of_birth, month_of_birth, day_of_birth)

    return name, date_of_birth


name, date_of_birth = get_birth_details()
print("Hello " + name + "!")
current_date = datetime.date.today()


def days_of_life(date_of_birth, current_date):
    return (current_date - date_of_birth).days


def physical_wave(age_in_days):
    return math.sin((2 * math.pi * age_in_days) / 23)


def emotional_wave(age_in_days):
    return math.sin((2 * math.pi * age_in_days) / 28)


def intellectual_wave(age_in_days):
    return math.sin((2 * math.pi * age_in_days) / 33)


def check_if_biorhythm_is_high(biorhythm_value):
    return biorhythm_value > 0.5


def check_if_biorhythm_is_low(biorhythm_value):
    return biorhythm_value < 0.5


print("Your date of birth is: " + str(date_of_birth.year) + "-" + str(date_of_birth.month) + "-" + str(date_of_birth.day))
print("Today is: " + str(current_date.year) + "-" + str(current_date.month) + "-" + str(current_date.day))
print("It's your " + str(days_of_life(date_of_birth, current_date)) + " day of life!")

if check_if_biorhythm_is_high(physical_wave(days_of_life(date_of_birth, current_date) + 1)):
    print("Your physical biorhythm is high! Seize the day")
elif check_if_biorhythm_is_low(physical_wave(days_of_life(date_of_birth, current_date))):
    print("Your physical biorhythm is low, but it's only number! Enjoy the day!")
    if check_if_biorhythm_is_high(physical_wave(days_of_life(date_of_birth, current_date) + 1)):
        print("Don't worry. Tomorrow will be better!")

if check_if_biorhythm_is_high(emotional_wave(days_of_life(date_of_birth, current_date))):
    print("Your emotional biorhythm is high! Seize the day")
elif check_if_biorhythm_is_low(emotional_wave(days_of_life(date_of_birth, current_date))):
    print("Your emotional biorhythm is low, but it's only number! Enjoy the day!")
    if check_if_biorhythm_is_high(emotional_wave(days_of_life(date_of_birth, current_date) + 1)):
        print("Don't worry. Tomorrow will be better!")

if check_if_biorhythm_is_high(intellectual_wave(days_of_life(date_of_birth, current_date))):
    print("Your intellectual biorhythm is high! Seize the day")
elif check_if_biorhythm_is_low(intellectual_wave(days_of_life(date_of_birth, current_date))):
    print("Your intellectual biorhythm is low, but it's only number! Enjoy the day!")
    if check_if_biorhythm_is_high(intellectual_wave(days_of_life(date_of_birth, current_date) + 1)):
        print("Don't worry. Tomorrow will be better!")
