# ----------------------------------------------------------
# Exercise 1
def display_message():
    print("I am learning about functions in this chapter.")


display_message()


# ----------------------------------------------------------
# Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")


favorite_book("The Lord of the Rings")


# ----------------------------------------------------------
# Exercise 3
def describe_city(city_name, country="Mauritius"):
    print(f"{city_name} is in {country}.")


describe_city("Rose Hill")

# ----------------------------------------------------------
# Exercise 4
import random


def gen_rand_int(value):
    second_value = random.randint(1, 100)

    if second_value == value:
        print(f"The two numbers are the same; {value}")
    else:
        print(f"The two numbers are different; {value} and {second_value}")

    return second_value


first_value = random.randint(1, 100)
second_value = gen_rand_int(first_value)


# ----------------------------------------------------------
# Exercise 5
def make_shirt(shirt_size="L", shirt_text="I love Python"):
    print(f"The size of the shirt is '{shirt_size}' and the text is '{shirt_text}'.")


make_shirt()
make_shirt("M")
make_shirt("S", "I love Java")
make_shirt(shirt_size="XXL", shirt_text="I love C++")

# ----------------------------------------------------------
# Exercise 6
magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]


# Method 1, regular function + loop
def show_magicians(name_list):
    # print(name_list) # Don't print the list itself

    # Add loop code to print individual name
    for name in name_list:
        print(name)


# show_magicians(magician_names)


# Method 2, map
def show_magicians_map(name):
    print(name)
    # return f"{name}"


# result = map(show_magicians_map, magician_names)
# list(result) # For some reason, this is important


# Method 3, *args
def show_magicians_args(*args):
    # print(args)
    if type(args[0]) == list:
        for name in args[0]:
            print(name)
    else:
        print(f"Beep boop beep, there is an error. This is not a list!")


show_magicians_args(magician_names, 2, 4, 5, 6, 7, 8)


def make_great(name_list):
    for i in range(len(name_list)):
        name_list[i] += " the Great"


make_great(magician_names)
show_magicians(magician_names)

# ----------------------------------------------------------
# Exercise 7

import random


def get_random_temp(season_int):
    """Generate a random float between -10 (inclusive) and 40 (inclusive/exclusive).
    Return the generated float.
    """

    spring = "spring"
    summer = "summer"
    autumn = "autumn"
    winter = "winter"

    season = ""
    if season_int >= 3 and season_int <= 5:
        season = spring
    elif season_int >= 6 and season_int <= 8:
        season = summer
    elif season_int >= 9 and season_int <= 11:
        season = autumn
    elif (season_int >= 1 and season_int <= 2) or season_int == 12:
        season = winter
    else:
        print(f"We received a bad value for season. ({season_int})")

    season_limits = {
        summer: {"lower": 33, "upper": 40},
        autumn: {"lower": 24, "upper": 33},
        winter: {"lower": -10, "upper": 17},
        spring: {"lower": 17, "upper": 24},
    }

    random_float = random.uniform(
        season_limits[season]["lower"], season_limits[season]["upper"]
    )
    # Math Notation:
    # [] Inclusive
    # () Exclusive
    return random_float


def main():
    # user_season = ""

    # while user_season not in ["summer", "autumn", "winter", "spring"]:
    #     user_season = input(
    #         "Please enter the season ('summer', 'autumn', 'winter', 'spring'): "
    #     ).lower()

    user_season_int = 0

    while user_season_int <= 0 or user_season_int >= 13:
        user_season_int = int(input("Please enter the season (1-12): "))

    random_temperature = get_random_temp(user_season_int)

    print(f"The temperature right now is {random_temperature} degrees Celsius.")

    if random_temperature < 0:
        print(f"Brrr, that’s freezing! Wear some extra layers today")
    elif random_temperature >= 0 and random_temperature < 16:
        print(f"Quite chilly! Don’t forget your coat")
    elif random_temperature >= 16 and random_temperature < 24:
        print(f"Nice weather")
    elif random_temperature >= 24 and random_temperature < 32:
        print(f"It's getting hot out here")
    elif random_temperature >= 32 and random_temperature < 40:
        print(f"It's way too hot, I'm staying at home.")
    else:
        print(f"Woops, something went wrong, the temperature is way too high!")


main()
