import datetime
import math


# Function to get user details: name and date of birth
def get_birth_details():
    """Prompt the user for their name and birthdate, and return these details."""
    name = input("What's your name? ")
    year_of_birth = int(input("What's your year of birth? "))
    month_of_birth = int(input("What's your month of birth? "))
    day_of_birth = int(input("What's your day of birth? "))

    date_of_birth = datetime.date(year_of_birth, month_of_birth, day_of_birth)
    return name, date_of_birth


# Function to calculate the total number of days since birth
def days_of_life(date_of_birth, current_date):
    """Calculate and return the number of days the user has lived."""
    return (current_date - date_of_birth).days


# Functions to calculate the biorhythm values (physical, emotional, intellectual)
def calculate_biorhythm_wave(age_in_days, cycle_length):
    """General function to calculate biorhythm wave for a given cycle."""
    return math.sin((2 * math.pi * age_in_days) / cycle_length)


def physical_wave(age_in_days):
    """Calculate the physical biorhythm wave (23-day cycle)."""
    return calculate_biorhythm_wave(age_in_days, 23)


def emotional_wave(age_in_days):
    """Calculate the emotional biorhythm wave (28-day cycle)."""
    return calculate_biorhythm_wave(age_in_days, 28)


def intellectual_wave(age_in_days):
    """Calculate the intellectual biorhythm wave (33-day cycle)."""
    return calculate_biorhythm_wave(age_in_days, 33)


# Helper functions to check if biorhythm is high, neutral, or low
def is_biorhythm_high(biorhythm_value):
    """Return True if the biorhythm value is high (> 0.5)."""
    return biorhythm_value > 0.5


def is_biorhythm_low(biorhythm_value):
    """Return True if the biorhythm value is low (< -0.5)."""
    return biorhythm_value < -0.5


def display_biorhythm_status(wave_value, wave_type, days_lived):
    """Print a motivational message based on the biorhythm wave's value."""
    if is_biorhythm_high(wave_value):
        print(f"Your {wave_type} biorhythm is high! Seize the day.")
    elif is_biorhythm_low(wave_value):
        print(f"Your {wave_type} biorhythm is low, but it's only a number! Enjoy the day.")
        # Encourage the user by checking tomorrow's value
        if is_biorhythm_high(calculate_biorhythm_wave(days_lived + 1, wave_type_cycle_length(wave_type))):
            print("Don't worry. Tomorrow will be better!")
    else:
        print(f"Your {wave_type} biorhythm is balanced today.")


# Function to map biorhythm type to its cycle length
def wave_type_cycle_length(wave_type):
    """Return the cycle length for the given biorhythm type."""
    cycle_lengths = {
        'physical': 23,
        'emotional': 28,
        'intellectual': 33
    }
    return cycle_lengths[wave_type]


# Main program execution
def main():
    # Get user details and calculate days of life
    name, date_of_birth = get_birth_details()
    print(f"Hello {name}!")

    current_date = datetime.date.today()
    days_lived = days_of_life(date_of_birth, current_date)

    # Display basic information
    print(f"Your date of birth is: {date_of_birth}")
    print(f"Today is: {current_date}")
    print(f"It's your {days_lived}th day of life!")

    # Calculate biorhythm values
    physical_biorhythm = physical_wave(days_lived)
    emotional_biorhythm = emotional_wave(days_lived)
    intellectual_biorhythm = intellectual_wave(days_lived)

    # Display motivational messages for each biorhythm
    display_biorhythm_status(physical_biorhythm, 'physical', days_lived)
    display_biorhythm_status(emotional_biorhythm, 'emotional', days_lived)
    display_biorhythm_status(intellectual_biorhythm, 'intellectual', days_lived)


# Run the main function when the script is executed
if __name__ == "__main__":
    main()

