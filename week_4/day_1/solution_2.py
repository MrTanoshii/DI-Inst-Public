"""
Credit: Dintu, Jacob
GitHub: https://github.com/jacobgreg27/DI-Bootcamp/tree/main/DI-Bootcamp-2/week-4/day-1/daily-challenge-week-4-day-1
"""


# Part 1
string = input("Write a text: ")

if len(string) < 10:
    print("string not long enough")

elif len(string) > 10:
    print("string too long")

# Part 2
else:
    print(string[0], string[-1])

# we find length since that is equal to our row as shown on line 16

length = len(string)
for row in range(length):
    # how many columns we need is shown by the fact that as we grow in rows, we are adding one more column to it
    for col in range(row + 1):
        # we print the character of the string col where col is the index
        print(string[col], end="")

        # print rows
    print()

import random

shuffled_string = "".join(random.sample(string, len(string)))

print(shuffled_string)
