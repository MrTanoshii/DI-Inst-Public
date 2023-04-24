# ----------------------------------------------------------
# Exercise 1
my_fav_numbers = {5, 8, 13, 55}
my_fav_numbers.add(3)
my_fav_numbers.add(1)
my_fav_numbers.remove(1)
friend_fav_numbers = {5, 8, 13, 55, 111}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# ----------------------------------------------------------
# Exercise 2
# No

# ----------------------------------------------------------
# Exercise 3
# Typo in question, remove the `;` from the basket list code
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(f"There are {basket.count('Apples')} Apples")
basket.clear()
print(basket)


# ----------------------------------------------------------
# Exercise 4
# Possible typo, swap part 2 and part 3 around

# 4.1
# A `float` contains decimal places after the whole numbers
# An `integer` is a whole number.

# 4.3
x = 1
my_list = []
for y in range(0, 9):
    my_list.append(x)
    x += 0.5
print(my_list)

# 4.2
my_list2 = [1]
count = 0
while count < 8:
    my_list2.append(my_list2[-1] + 0.5)
    count += 1
print(my_list2)

# ----------------------------------------------------------
# Exercise 5
for x in range(1, 21):
    print(f"{x}", end="->")
print()

for x in range(1, 21):
    if x % 2 == 0:
        print(f"{x}", end="->")
print()

# ----------------------------------------------------------
# Exercise 6
user_name = ""
while user_name != "vincent":
    user_name = input("Enter your name ('Vincent' to exit): ").lower()

# ----------------------------------------------------------
# Exercise 7
fav_fruits = (
    input("Enter your favourite fruits (separated by commas): ").lower().split(",")
)
user_fav_fruit = input("Enter a fruit name: ")
if user_fav_fruit in fav_fruits:
    print("You chose one of your favourite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it too!")

# ----------------------------------------------------------
# Exercise 8
topping_list = []
while True:
    user_input = input("Enter a pizza topping ('quit' to stop): ")
    if user_input.lower() == "quit":
        break
    topping_list.append(user_input)
    print(f"Adding {topping_list[-1]} to your pizza...")

print(f"Your total cost is {10 + 2.5 * len(topping_list)}")

# ----------------------------------------------------------
# Exercise 9

total_cost = 0
while True:
    user_age_str = input("Enter the age of the person (0 to quit): ")
    if user_age_str == "0" or not user_age_str.isnumeric():
        break
    user_age = int(user_age_str)
    if user_age < 3:
        total_cost += 0
    elif user_age < 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"The total cost is ${total_cost}")

teen_list = ["Adam", "Bill", "Charlie", "David", "Ethan"]
temp_list = []
for x in range(0, len(teen_list)):
    teen_age = int(input(f"Enter the age of {teen_list[x]}: "))
    if teen_age >= 16 and teen_age <= 21:
        print(f"{teen_list[x]} is permitted to watch the movie")
        temp_list.append(teen_list[x])
    else:
        print(f"{teen_list[x]} is not permitted to watch the movie")

teen_list = temp_list
print(f"The final list is: {teen_list}")

# ----------------------------------------------------------
# Exercise 10
sandwich_orders = [
    "Tuna sandwich",
    "Avocado sandwich",
    "Egg sandwich",
    "Sabih sandwich",
    "Pastrami sandwich",
]
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order}")
    finished_sandwiches.append(current_order)

# ----------------------------------------------------------
# Exercise 11
sandwich_orders = [
    "Tuna sandwich",
    "Avocado sandwich",
    "Pastrami sandwich",
    "Egg sandwich",
    "Sabih sandwich",
    "Pastrami sandwich",
    "Pastrami sandwich",
]
finished_sandwiches = []

print("We ran out of Pastrami!")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order}")
    finished_sandwiches.append(current_order)
