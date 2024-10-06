import math
from datetime import date, datetime


# Function to calculate the number of days from birth to today
def calculate_days_alive(birthdate):
    today = date.today()
    delta = today - birthdate
    return delta.days


# Function to calculate biorythms
def calculate_biorhythm(day_of_life, cycle_length):
    return math.sin((2 * math.pi * day_of_life) / cycle_length)


# Main program
def main():
    # Get user input
    name = input("What is your name? ")
    birth_year = int(input("What year were you born? "))
    birth_month = int(input("What month were you born? "))
    birth_day = int(input("What day were you born? "))

    # Create a date object for the birthdate
    birthdate = date(birth_year, birth_month, birth_day)

    # Calculate days of life
    days_alive = calculate_days_alive(birthdate)

    # Calculate biorythms
    physical_score = calculate_biorhythm(days_alive, 23)
    emotional_score = calculate_biorhythm(days_alive, 28)
    intellectual_score = calculate_biorhythm(days_alive, 33)

    # Print greetings and results
    print(f"\nHello, {name}! Today is day {days_alive} of your life.")
    print(f"Your biorythms for today are as follows:")
    print(f"Physical: {physical_score:.2f}")
    print(f"Emotional: {emotional_score:.2f}")
    print(f"Intelectual: {intellectual_score:.2f}")

    # Analyze biorythms and provide feedback
    def evaluate_biorhythm(score, next_day_score):
        if score > 0.5:
            print("Your score is high! You're feeling great!")
        elif score < -0.5:
            print("Your score is low. Take it easy today.")
            if next_day_score > score:
                print("Don't worry. Tomorrow will be better!")
            else:
                print("Hang in there, things may improve soon.")
        else:
            print("You're having a balanced day.")

    # Calculate next day's scores
    next_physical_score = calculate_biorhythm(days_alive + 1, 23)
    next_emotional_score = calculate_biorhythm(days_alive + 1, 28)
    next_intellectual_score = calculate_biorhythm(days_alive + 1, 33)

    # Evaluate today's and tomorrow's biorythms
    print("\nEvaluating physical state:")
    evaluate_biorhythm(physical_score, next_physical_score)

    print("\nEvaluating emotional state:")
    evaluate_biorhythm(emotional_score, next_emotional_score)

    print("\nEvaluating intellectual state:")
    evaluate_biorhythm(intellectual_score, next_intellectual_score)


# Run the program
if __name__ == "__main__":
    main()
