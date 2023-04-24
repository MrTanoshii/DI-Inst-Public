# ----------------------------------------------------------
# Exercise 1

cars_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = cars_str.split(", ")

print(f"There are {len(cars_str)} manufacturers of cars in the list.")
print(f"The reversed list is: {sorted(cars_list,reverse=True)}")

o_list = []
o_list += [
    character
    for manufacturer in cars_list
    for character in manufacturer
    if character == "o"
]

print(o_list)

print(f"There are {len(o_list)} 'o's in the manufacturers' names")

i_in_manufacturer_count = 0
for manufacturer in cars_list:
    has_i = False
    for character in manufacturer:
        if character == "i":
            has_i = True
            break
    if has_i:
        i_in_manufacturer_count += 1

print(
    f"There are {len(cars_list) - i_in_manufacturer_count} manufacturers without the 'i' in their names"
)

# Bonus

bonus_list = [
    "Honda",
    "Volkswagen",
    "Toyota",
    "Ford Motor",
    "Honda",
    "Chevrolet",
    "Toyota",
]
bonus_list = list(set(bonus_list))
print(bonus_list)

display_str = ""
for el in bonus_list:
    display_str += el
    display_str += ", "
display_str = display_str[:-2]
print(display_str)
print(f"There are {len(bonus_list)} manufacturers")

# Yet another bonus
asc_list = sorted(bonus_list)
for el in asc_list:
    for x in range(len(el) - 1, -1, -1):
        print(el[x], end="")
    print(", ", end="")
