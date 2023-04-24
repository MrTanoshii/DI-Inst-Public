# ----------------------------------------------------------
# Exercise 1
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

ex_1_dict = zip(keys, values)
print(dict(ex_1_dict))

# ----------------------------------------------------------
# Exercise 2

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0

for name, age in family.items():
    ticket_cost = 15
    if age < 3:
        ticket_cost = 0
    elif age < 12:
        ticket_cost = 10

    total_cost += ticket_cost
    print(f"{name} ({age}) has to pay ${ticket_cost}")

print(f"The total cost is ${total_cost}")

# Bonus
# dynamic_family = {}
# while True:
#     name = input("Enter a name (leave empty to exit): ")
#     if name == "":
#         break
#     age = int(input("Enter an age: "))
#     dynamic_family[name] = age

# ----------------------------------------------------------
# Exercise 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}

brand["number_stores"] = 2
print(f"Zara clients are {brand['type_of_clothes']}")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][-1])
print(f"Major colors in the US: {brand['major_color']['US']}")
print(len(brand))
print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000,
}

brand.update(more_on_zara)
print(brand["number_stores"])

# ----------------------------------------------------------
# Exercise 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {}
for index in range(len(users)):
    disney_users_A[users[index]] = index
print(disney_users_A)

disney_users_B = {}
for index in range(len(users)):
    disney_users_B[index] = users[index]
print(disney_users_B)


disney_users_C = {}
sorted_users = sorted(users)
for index in range(len(sorted_users)):
    disney_users_C[sorted_users[index]] = index
print(disney_users_C)

disney_users_D = {}
for index in range(len(users)):
    if "i" in users[index]:
        disney_users_D[users[index]] = index
print(disney_users_D)

disney_users_E = {}
for index in range(len(users)):
    if users[index][0] in ["m", "p"]:
        disney_users_E[users[index]] = index
print(disney_users_E)
