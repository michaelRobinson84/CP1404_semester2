"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():

    score = float(input("Enter score: "))

    str_score_status = determine_score_status(score)

    print("Your score status is " + str_score_status)

    random_score = random.randint(0, 100)

    str_random_score_status = determine_score_status(random_score)

    print("Your random score status is " + str_random_score_status)


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
