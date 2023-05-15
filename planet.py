import random

# dictionary containing planet names and their corresponding descriptions
planets = {
    "Mercury": "The smallest planet in our solar system and closest to the sun.",
    "Venus": "The second planet from the sun and the hottest planet in our solar system.",
    "Earth": "The third planet from the sun and the only planet known to support life.",
    "Mars": "The fourth planet from the sun and also known as the 'Red Planet'.",
    "Jupiter": "The largest planet in our solar system and known for its many moons.",
    "Saturn": "The sixth planet from the sun and known for its beautiful rings.",
    "Uranus": "The seventh planet from the sun and known for its extreme tilt.",
    "Neptune": "The eighth planet from the sun and known for its blue color."
}

# function to ask a planet question and get user's answer
def ask_question(planet):
    print(f"What is {planet}'s description?")
    answer = input("Answer: ")
    return answer

# function to check if user's answer is correct
def check_answer(planet, answer):
    if answer.lower() == planets[planet].lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is: {planets[planet]}")
        return False

# list of planet names
planet_names = list(planets.keys())

# shuffle the list of planet names
random.shuffle(planet_names)

# iterate through the shuffled list of planet names and ask a question for each planet
for planet in planet_names:
    answer = ask_question(planet)
    check_answer(planet, answer)
