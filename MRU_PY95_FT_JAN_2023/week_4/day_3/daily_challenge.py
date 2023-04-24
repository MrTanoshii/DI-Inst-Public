# ----------------------------------------------------------
# Challenge 1

user_input = input("Enter a word please: ")  # dodo, froggy, grapes
char_index_dict = {}

for letter_position, letter in enumerate(
    user_input
):  # looping through letters of the user input
    print(f"At position {letter_position}, we have the letter {letter}")
    if (
        letter in char_index_dict.keys()
    ):  # Checking if the letter exists as a key in the dict
        char_index_dict[letter].append(
            letter_position
        )  # e.g. char_index_dict["d"], Accessing the dictionary and add the position of the letter to the current list at the end
    else:  # Letter does not exist as a key in the dict
        char_index_dict[letter] = [
            letter_position
        ]  # Make a new key using letter and assign the letter position value as a list

print(char_index_dict)

# Extra, rebuild the word from the dictionary
# Find out the length of the word
word_len = 0
for key, position_list in char_index_dict.items():
    for position in position_list:
        if position > word_len:
            word_len = position
word_len += 1
print(f"The word has length {word_len}")

rebuild_index = 0
rebuilt_word = ""
for rebuild_index in range(0, word_len):
    found_letter = False
    for key, position_list in char_index_dict.items():
        for position in position_list:
            if position == rebuild_index:
                rebuilt_word += key
                rebuild_index += 1
                found_letter = True
                break
        if found_letter:
            break

print(f"The rebuilt word is : {rebuilt_word}")

# ----------------------------------------------------------
# Challenge 2

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20",
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2",
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200",
}

wallet_str = input("Enter the amount of cash you have on you: ")
wallet_int = int(wallet_str.replace("$", "").replace(",", ""))

affordable_items = []
for item, cost_str in items_purchase.items():
    cost_int = int(cost_str.replace("$", "").replace(",", ""))
    if wallet_int >= cost_int:
        print(f"You can buy {item}")
        affordable_items.append(item)

if len(affordable_items) > 0:
    affordable_items.sort()
    print(f"You can buy {affordable_items}")
else:
    print("You can buy nothing ;_;")
