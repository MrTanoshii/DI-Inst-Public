"""
Credit: jhurry , khavind dev
GitHub: https://github.com/Hemlesh18/DI_Bootcamp/blob/main/week4/daily-challenge/file.py
"""

# Part 1

sentence = input("Enter a string of 10 characters long:")  # Getting user input

if len(sentence) < 10:
    print("String not long enough")
elif len(sentence) > 10:
    print("string too long")
else:
    # Part 2
    print(f"{sentence[0]}\n {sentence[-1]}")

    # sentence[len(sentence) - 1] # last character

# Part 3
result = " "
for character in sentence:
    result += character  # result = result + character
    print(result)

# Part 4
import random

str_list = list(sentence)
random.shuffle(str_list)
print(f"Shuffled list: {str_list}")
str_final = "".join(str_list)
print(f"Final answer: {str_final}")
