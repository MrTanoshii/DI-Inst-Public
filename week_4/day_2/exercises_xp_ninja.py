# ----------------------------------------------------------
# Exercise 1

import math

num_list_str = input("Please input comma separated numbers: ")
num_list = num_list_str.split(
    ","
)  # Split the string into individual strings separated by ","

c = 50
h = 30

result_list = []
for d in num_list:
    result_list.append(
        int(math.sqrt((2 * c * int(d)) / h))
    )  # Append the result to the result list
print(result_list)

# ----------------------------------------------------------
# Exercise 2

var_list = [
    [3, 47, 99, -80, 22, 97, 54, -23, 5, 7],
    [44, 91, 8, 24, -6, 0, 56, 8, 100, 2],
    [3, 21, 76, 53, 9, -82, -3, 49, 1, 76],
    [18, 19, 2, 56, 33, 17, 41, -63, -82, 1],
]
for el_list in var_list:
    print()
    print("New list")

    print(f"List: {el_list}")
    print(f"Desceding list: {sorted(el_list, reverse=True)}")
    print(f"Sum: {sum(el_list)}")
    print(f"First and Last: {el_list[0]} {el_list[-1]}")

    # This uses something called a list comprehension
    # See: https://www.w3schools.com/python/python_lists_comprehension.asp
    greater_than_50 = [num for num in el_list if num > 50]
    print(f"> 50: {greater_than_50}")

    smaller_than_10 = [num for num in el_list if num < 10]
    print(f"< 10: {smaller_than_10}")

    print(f"Squared: {[num**2 for num in el_list]}")

    print(f"List with no dupes: {set(el_list)} | length: {len(set(el_list))}")

    print(f"Average Built-in: {sum(el_list) / len(el_list)}")
    print(f"Maximum Built-in: {max(el_list)}")
    print(f"Minimum Built-in: {min(el_list)}")

    average = 0
    maximum = 0
    minimum = 0
    for num in el_list:
        average += num
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    average = average / len(el_list)

    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

# Bonus 2: It will work the same

# ----------------------------------------------------------
# Exercise 3

interesting_text = "Alarmed by A.I. Chatbots, Universities Start Revamping How They Teach \
\
With the rise of the popular new chatbot ChatGPT, colleges are restructuring some courses and taking preventive measures."

print()
print("Interesting Text")
print(f"Characters: {len(interesting_text)}")

# Note: this will not provide appropriate results with the current text as the text contains abbreviations.
# Assuming sentences are separated by a period or a new line
sentence_count = len(interesting_text.split("\n")) + len(interesting_text.split("."))
print(f"Sentences: {sentence_count}")

word_count = len(interesting_text.split(" "))
print(f"Words: {word_count}")
unique_word_count = len(set(interesting_text.split(" ")))
print(f"Unique words: {unique_word_count}")

import copy

# I am making a copy of the string so that I do not modify the original string
interesting_text_copy = copy.deepcopy(interesting_text)
interesting_text_copy.replace(" ", "")

print(f"Non whitespace: {len(interesting_text_copy)}")
print(f"Average words per sentence: {word_count / sentence_count}")
print(f"Non-unique words: {word_count - unique_word_count}")

# ----------------------------------------------------------
# Exercise 4

input_text = input("Please input a string: ")
print()
for word in input_text.split():
    print(f"{word}: {input_text.count(word)}")
