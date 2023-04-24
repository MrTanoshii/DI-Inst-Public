# my_dict = {
#     "students": ["Cynthia", "Sebastien", "Alexis"],
#     "grades": [90, 80, 100],
#     "food": ["pizza", "pasta"],
#     "pass_grade": 70,
#     "classes": {
#         "math": "Algebra",
#         "science": "Physics",
#     },
#     "test213_#@$*&#@": "fdskfjskd",
#     " ": "fdsfds",
#     "tuple": (43543534, 32432.23, "test"),
# }

# # print(my_dict)

# # print(my_dict["students"])
# # print(my_dict["classes"]["math"])
# # print(my_dict["grades"][-1])

# # print(my_dict["gradess"]) # This will fail because the key doesn't exist

# # my_tuple = (100, "dsfdsfsdf", 32432.543, True)
# # print(my_tuple)

# # a, b, c, d = my_tuple

# # print(a, b, c, d)
# print(my_dict[" "])

# print(my_dict.items())

# for key123, value in my_dict.items():
#     print(f"{key123} -> {value}")
#     print(f"The type of the value is: {type(value)}")
#     if type(value) == dict:
#         print(f"Hey this was a dictionary with nested value")
#         print(my_dict[key123])

# for key, value in my_dict["classes"].items():
#     print(f"{key} contains {value}")

# for key, _ in my_dict.items():
#     print(f"{key}")

# # print(my_dict.keys())

# sample_dict = {
#     "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
# }

# print(sample_dict["class"])
# print(sample_dict["class"]["student"])
# print(sample_dict["class"]["student"]["marks"]["history"])

# test_dict = {
#     "test1": {"test": {"test": {}}},
#     "test2": 213213,
#     "test3": "Hello",
#     "test4": 123.09,
# }

# # test_dict["test"] = {"test": {"test": {}}}
# # test_dict["test"] = 213213
# # test_dict["test"] = "Hello"
# # test_dict["test"] = 123.09

# # print(test_dict)

# # test_dict["test1"] = 45
# # test_dict["test2"] = ("dsfdsfds", 324324, 32432.97324)
# # print(test_dict)

# test_dict["names"] = ["Khavind", "Tushil", "Cynthia"]
# del test_dict["test1"]
# test_dict.pop("test2")
# test_dict[
#     "test3"
# ] = ""  # This does not delete the key:value pair, it just removes the value
# print(test_dict)

# my_set = set()
# my_set.add("test")
# my_set.add("tes1")
# my_set.add("test2")
# my_set.add("test3")
# my_set.add("test4")
# my_set.add("test5")
# my_set.add("test")
# my_set.add("test")

# print(my_set)

# names = ["Vincent", "Yushi", "Jacob", "David"]
# if "vincent".capitalize() in names:
#     print("This name was in the list")


# my_dict = {"names": ["David", "Alexis", "Raees", "Shabneez", "Martine", "Soubhug"]}

# if "names" in my_dict:
#     print(f"This exists: {my_dict['names']}")

# print(my_dict.items())

# my_dict2 = {"test": "testing"}

# my_dict.update(my_dict2)

# # x = del my_dict['test']
# x = my_dict.pop("names")
# print(x)
# try:
#     my_dict.pop("namestest345435")
# except:
#     # raise KeyError("This is an error because of the key")
#     print("ok that went wrong")
# print(my_dict)

# test_list = ["test", "1", "2", "3"]

# print(dir(test_list))  # Look for __iter__

# for item in enumerate(test_list):
#     print(item[-1])

# # print(dir(32432))
# # for x in enumerate(32432):
# #     print(x)

# for item in test_list:
#     print(item)

# my_tuple = ("sdfds", "'dsfdsf")
# a, b = my_tuple

# init_value = 12345
# rebuilt_value = 0

# for index, value in enumerate(str(init_value)):
#     print(f"The index and values are: {index} , {value}")
#     position_of_int = len(str(init_value)) - (index + 1)
#     power_of_ten = 10 ** (position_of_int)
#     rebuilt_value += int(value) * power_of_ten
#     print(f"The current value of rebuilt is: {rebuilt_value}")

# list1 = [1, 2, 3]
# list2 = ["Cynthia", "Jacob", "Alexis"]
# list3 = [99.9, 85.8, 79.2]

# for item in zip(list1, list2, list3):
#     print(item)
#     continue

# counter = 0
# while counter <= 10:
#     print(counter)
#     counter += 2
#     if counter == 7:
#         break
# else:
#     print("This for loop is complete and never had the value 7")

# print("This for loop is complete")

# my_number = "1234"
# my_list = []

# # for num in my_number:
# #     my_list.append(num)

# my_list = [(int(num) * 100) for num in my_number]

# print(my_list)


# another_list = [x + 10 for x in range(100)]  # 0 - 99
# print(another_list)

# another_list = [x + 10 for x in range(200) if x / 2 > 10]
# print(another_list)

# my_list_no_2 = []

# for x in [1, 2, 3]:
#     for y in [100, 200, 300]:
#         my_list_no_2.append(x * y)

# print(my_list_no_2)


# my_list_no_2_list_comprehension = []
# my_list_no_2_list_comprehension = [x * y for x in [1, 2, 3] for y in [100, 200, 300]]
# print(my_list_no_2_list_comprehension)

# 2022
family_age = {"Lea": 12, "Mark": 25, "George": 50}

new_year = 1

# 2023
new_family_age = {name: age + new_year for (name, age) in family_age.items()}

# 2024
newest_new_family_age = {}
for name, age in new_family_age.items():
    # newest_new_family_age[name] = age + new_year
    name: age + new_year

print(newest_new_family_age)
