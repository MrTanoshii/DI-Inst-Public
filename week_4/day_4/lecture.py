# # Week 4 Day 3 Daily Challenge, Challenge 2

# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

# wallet_str = input("Enter your wallet amount: ")
# wallet = int(wallet_str.replace("$", ""))

# affordable_items = []

# # key is the item name
# # value is the cost price
# for key, value in items_purchase.items():
#     print(key, "->", value)

#     cost_price_str = value.replace("$", "")
#     cost_price_str = cost_price_str.replace(",", "")

#     cost_price = int(cost_price_str)

#     if wallet >= cost_price:
#         # I can afford this
#         affordable_items.append(key)

# print(sorted(affordable_items))
# # print(affordable_items)
# # affordable_items.sort()
# print(affordable_items)

# ---------------------------------
# # David's method, Challenge 2

# # dictionary // list of items
# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1000", "Fertilizer": "$20"}

# # declaring value for wallet
# wallet = "$300"

# # converting string value of wallet to integer as comparing was not working and removing "$" symbol
# wallet = int(wallet.replace("$", ""))

# # looping through dictionary with list to make a copy of the dictionary or error: the size of the dictionary, will be encounter
# for item in list(items_purchase):
#     # converting string value of price to integer as comparing was not working and removing "$" symbol
#     # getting value with .get(item)
#     price = int(items_purchase.get(item).replace("$", "").replace(",", ""))

#     # if the price of the product is higher than wallet pop that item from dictionary
#     if price > wallet:
#         items_purchase.pop(item)

# # if the length of the dictionary is "0" print: Nothing
# if len(items_purchase) == 0:
#     print("Nothing")

# # printing the list of item purchasale
# print(sorted(items_purchase.keys()))

# ------------------


# def say_hello():
#     """A function that says hello"""
#     print("Hello!")
#     x = 10
#     print(f"X is {x}")


# say_hello
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()
"""
dsfdfds
fdsfdsfds
fdsfsd
"""


def say_hello2():
    print("This is hello 2")


# say_hello()
# say_hello2()

# ---------------


def say_hello_user(greeting, username="Default username"):
    """Say hello to the user"""
    print(f"{greeting} {username}")
    # print("Good morning " + username)
    # print(greeting + " " + username)


# say_hello_user("Vincent")
# say_hello_user()
# say_hello_user("Martine")
# say_hello_user("Jacob")
# say_hello_user("Ra'ees")

# say_hello_user("Good night", "Khavind", "testestest", "testestest", "testestest")
# say_hello_user("Khavind", "Good night")
# say_hello_user("Good evening")
# say_hello_user(456456456456)


def seasonal_greeting(greeting="Howdy", season="Summer"):
    print(f"{greeting}, the season is {season}")


# seasonal_greeting()
# seasonal_greeting("Hello", "Autumn")
# seasonal_greeting("Good night", "KFC")
# seasonal_greeting(season="Winter", greeting="Good evening")
# seasonal_greeting("Good evening", "Winter")
# seasonal_greeting(season="Spring")

# x = 1000
# result = 100


# def calculate_times_2(value=10):
#     x = 2
#     result = value * x
#     print(result)


# calculate_times_2(50)
# print(x)
# # print(result)


# def test():
#     def nested_test():
#         def nested_test1():
#             def nested_test2():
#                 def nested_test3():
#                     def nested_test4():
#                         def nested_test5():
#                             def nested_test6():
#                                 print("hello")
#                             nested_test6()

#                         nested_test5()

#                     nested_test4()

#                 nested_test3()

#             nested_test2()

#         nested_test1()

#     nested_test()


# test()


def calculate_times_10(value):
    """Calculate the value times 10 and return the result."""

    result = value * 10
    totally_not_useful_information = "This is not useful"
    # print(result)
    return value, result, totally_not_useful_information


# value, value_multipled, why_am_i_getting_this_info = calculate_times_10(
#     1
# )  # Returning (1, 10 , "This is not useful")
# print(f"{value} x10 = {value_multipled} | {why_am_i_getting_this_info}")
# print(calculate_times_10(1))


# my_tuple = ("a", "b", "c", "D")
# a, b, c, d = my_tuple
# print(a)
# print(b)
# print(c)
# print(d)


def calculate(a, b, method):
    addition = substration = None

    if method == "add":
        addition = a + b
    elif method == "remove":
        substration = a - b
    return addition, substration


# addition, substration = calculate(10, 20, "add")
# print(addition, substration)
# addition, substration = calculate(10, 20, "remove")
# print(addition, substration)


# # Real world example of using default values and an if statement
# def add_2_numbers(a, b, debug=False):
#     """
#     Add 2 numbers together.

#     Keyword Arguments:
#     a: int
#     b: int
#     debug: bool (default: False)

#     Return:
#     result: int
#     """
#     a = a + b

#     if debug:
#         print(a)

#     return a


# x = [10]
# y = x
# print(x)
# # print(add_2_numbers(x, 20))
# y.append(50)
# print(x)
# print(y)

# add_2_numbers(10, 5, True)
# add_2_numbers(10, 5)

# name_list = ["Sebastien", "Vincent"]
# name_list.sort()
# sorted(name_list)

# def greet_users(users):  # users should be a list
#     for user in users:  # Because it's a list, we can loop through it
#         print(
#             "Hello " + user.title() + " !"
#         )  # For each user, print "hello" and then his name


# usernames = ["steve", "stan", "debbie"]
# greet_users(usernames)

# x = 10


# def my_f1():
#     print("Hello")


# def my_f2():
#     print("Word")


# def my_f3():
#     print("This is Rick!")


# list_of_functions = [my_f1, my_f2, my_f3]

# for function in list_of_functions:
#     print(function())

# unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
# completed_models = []


# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design until none are left.
#     Move each design to completed_models after printing.
#     """

#     while len(unprinted_designs) != 0:
#         current_design = unprinted_designs.pop()
#         completed_models.append(current_design)

#     return unprinted_designs


# def show_completed_models(completed_models):
#     """
#     Show all the models that were printed.
#     """

#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)


# abc = unprinted_designs.copy()
# show_completed_models(completed_models)
# copied_list = print_models(abc, completed_models)
# show_completed_models(completed_models)

# print(copied_list)
# print("---dsgfdgfdgfdgdfgfd-")
# print(unprinted_designs)
# print("---dsgfdgfdgfdgdfgfd-")
# print(completed_models)


# def check_arguments(value, *args):
#     print(f"These are the arguments {value} {args}")


# check_arguments(23432, 432432, 432432)


# def check_keywordedarguments(**kwargs):
#     print(kwargs)
#     if "age" in kwargs.keys():
#         print(kwargs["age"])


# my_dict = {"name": "Sarah", "age": 24}

# check_keywordedarguments(sdkhfksjdkfds=my_dict, pet="cat", car="BMW", wallet=0)
# >> {'name': 'Sarah', 'age': 24} // You get a dictionary


# def test_func(greeting, *args, **testkwargs):
#     print(f"Greeting is: {greeting} | Args are: {args} | Kwargs are: {testkwargs}")


# test_func("Hello", 50, 100)
# test_func("Hello World", 50, 100, age="42", name="Fissel")
# list_str = [
#     "Sebastien",
#     "Yushi",
#     "Martine",
#     "Jacob",
#     "Ra'ees",
#     "Khavind",
#     "Alexis",
#     "Cynthia",
#     "Shabneez",
#     "David",
#     "Soobhug",
# ]
# # "sdfsdfdsf".capitalize()
# # list_str.sort()
# # sorted(list_str)


# def list_to_upper(list_str):
#     """Converts a list of strings into a list of uppercased strings."""
#     # Ra'ees # upper[list_str]
#     # Jacob & Martine & Sebastien
#     for x in list_str:
#         y = x.upper()
#         print(y)


# def to_upper(string):
#     """Converts a string into an uppercased string."""
#     return string.upper()


# # list_to_upper(list_str)

# result = map(to_upper, list_str)
# print(list(result))


# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]


# def starts_with_A(s):
#     # if s[0] == "A":
#     #     return s
#     # else:
#     #     return None
#     return s[0] == "A"


# filtered_object = filter(starts_with_A, fruit)

# print(list(filtered_object))

# filtered_object = filter(lambda s: s[0] == "A", fruit)
# print(list(filtered_object))

# # from functools import reduce


# # def sum_numbers(first, second):
# #     return first + second


# # num_list = [10, 20, 50, 80, 120, 160]
# # result = reduce(sum_numbers, num_list)

# # print(result)


# def test_function(user):
#     print(f"Hello {user}")


# x = lambda user: print(f"Hello {user}")

# x("Raees")


list_str = [
    "Sebastien",
    "Yushi",
    "Martine",
    "Jacob",
    "Ra'ees",
    "Khavind",
    "Alexis",
    "Cynthia",
    "Shabneez",
    "David",
    "Soobhug",
    "Tushil",
]


def check_letters(name):
    # if len(name) <= 6:
    #     return name
    # else:
    #     return None
    return len(name) <= 6


filtered_object = filter(check_letters, list_str)
x = list(filtered_object)
print(x)


def say_hello(name):
    # print(f"Hello {name}")
    return f"Hello {name}"


mapped_object = map(say_hello, x)
print(list(mapped_object))
