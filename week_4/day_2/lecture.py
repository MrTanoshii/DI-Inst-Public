# # List []
# my_name = "Jack"
# hello = "Hello World"
# my_age = 27
# my_list = [my_name, my_age, hello]

# # my_name, my_age
# print(my_list[0:2])

# # my_age, hello
# print(my_list[1:3])

# # my_name, hello
# print(my_list[0:4:2])

# sequence_name[start_index:end_index:step]

# # hello
# print(my_list[-1])

# # Tuples ()
# my_tuple = (1 + 3, 2.7, "Thursday")
# print(my_tuple)
# print(my_tuple[0])

# Strings
# my_string = "Yay"
# my_string_2 = "^.^"
# my_string_3 = my_string + my_string_2
# my_string_3 = my_string_2 + my_string
# list(my_string).extend(list(my_string_2))

# print(my_string)

# print(f"Length of my_list: {len(my_list)}")


# int_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # print 0-5
# print(int_list[0:6:1])

# # print 3-5
# print(int_list[3:6:1])

# # print 0, 2, 4
# print(int_list[0:6:2])
# print(int_list[0:5:2])

# # print 9, 7, 5, counting from the end of the list
# print(int_list[-1:-6:-2])

# # print 9, 6, 3
# print(int_list[-1:0:-3])

# print(int_list[0:-5:2])  # Not recommended

# Stepping different values
# for x in range(1, 10):
#     if x < len(int_list):
#         print(int_list[0 : len(int_list) : x])

int_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# int_list[0] += 10  # Incrementing the first value by 10
# print(int_list)

# I want to add things to my list
print(f"Starting length: {len(int_list)}")
int_list.insert(7, 100)
int_list.insert(0, -1)  # Add to the beginning
int_list.append(-1)  # Add to the end
print(int_list)
print(f"End length: {len(int_list)}")

# remove() uses the value that you want to remove
int_list.remove(100)
print(int_list)
int_list.remove(8)
print(int_list)

# pop() uses the index that you want to remove
int_list.pop(0)
print(int_list)
int_list.pop(-1)
print(int_list)

list_1 = [1, 2]
list_2 = [3, 4]
list_1.extend(list_2)

print(list_1)

# unsorted_list = [5, 7,8,  3, 3.8, "hello", "hello", 3.8, 43985798435, 1, 12]
unsorted_list = [5, 7, 8, 3, 3.8, 3.8, 43985798435, 1, 12]
print(unsorted_list)

# Sorted ascending
print(sorted(unsorted_list))
# Sorted descending
print(sorted(unsorted_list, reverse=True))

alpha_list_unsorted = ["afdgfd", "gfdgfd", "dfgb", "i"]
print(alpha_list_unsorted)
print(sorted(alpha_list_unsorted))
print(sorted(alpha_list_unsorted, reverse=True))

date_list_unsorted = ["07-02-2023", "10-02-2021", "04-12-2022"]
print(date_list_unsorted)
print(sorted(date_list_unsorted))

us_date_list_unsorted = ["2023-02-07", "2021-02-10", "2022-12-04"]
print(us_date_list_unsorted)
print(sorted(us_date_list_unsorted))

# Exercise
list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1.index(20))

# Extra exercise, finding all indexes of 20
indexes_of_20 = []
number_of_removed_values = 0
while 20 in list1:
    index_of_first_20_found = (
        list1.index(20) + number_of_removed_values
    )  # Finding the first index of 20
    indexes_of_20.append(index_of_first_20_found)
    # print(f"Indexes of 20: {indexes_of_20}")
    list1.pop(indexes_of_20[-1] - number_of_removed_values)  # Remove the found value
    number_of_removed_values += 1
print(f"Indexes of 20: {indexes_of_20}")

# First loop
# list1 looks like: [5, 10, 15, 20, 25, 50, 20]
# index(20) == 3
# number_of_removed_values == 0
# index_of_first_20_found = 3
# indexes_of_20 = [3]
# pop(3 - 0)

# Second loop
# list1 looks like: [5, 10, 15, 25, 50, 20]
# index(20) == 5
# number_of_removed_values == 1
# index_of_first_20_found = 6
# indexes_of_20 = [3, 6]
# pop(6 - 1)

# tuples

my_tuple = (5, 6, 7)
print(my_tuple)
print(my_tuple[0])

a_tuple = (10, 20, 30, 40)

# a, b, c, d = a_tuple
# a_tuple[0] = 100 # this will not work!
d, b, c, a = a_tuple
print(a)
print(b)
print(c)
print(d)

test_list = [1, 2, 3, 4]
test_list[0] = 100
a, b, c, d = test_list
print(a)
print(b)
print(c)
print(d)

my_set = set()  # this is an empty set
my_set.add("Khavind")
my_set.add("Shabneez")
print(my_set)

my_other_set = {"Chyama", "Cynthia"}
print(my_other_set)

my_dupe_set = {"Chyama", "Cynthia", "Chyama", "Cynthia"}
print(my_dupe_set)

my_int_set = {1, 2, 3, 1, 2, 3, 2, 2, 2, 2}
print(my_int_set)

# print(x)
for x in a_tuple:
    print(x)

# this is outside the for loop
print(x)

for y in my_int_set:
    print(f"This is my int set: {y}")

for subscriber in my_dupe_set:
    # some code related to sending emails
    pass


my_int_list = [1, 2, 3, 1, 2, 3, 2, 100, 2, 2, 2]
my_int_list_max = max(my_int_list)
print(f"My maximum value is: {my_int_list_max}")
print(f"My minimum value is: {min(my_int_list)}")
print(f"My sum is: {sum(my_int_list)}")
print(f"My avg is: {sum(my_int_list)/ len(my_int_list)}")

# Finding the sum
my_sum = 0
for x in my_int_list:
    my_sum += x  # my_sum = my_sum + x
print(f"My sum is: {my_sum}")

# Finding the max
my_int_list = [1, 2, 3, 1, 2, 3, 2, 100, 2, 2, 2]
my_max = 0
for x in my_int_list:
    if x > my_max:
        my_max = x

# my_max = 1
# my_max = 2
# my_max = 3
# my_max = 3
# my_max = 3
# my_max = 3
# my_max = 3
# my_max = 100
# my_max = 100
# my_max = 100
# my_max = 100

print("My maximum value is " + str(my_max))

# Finding the min
my_int_list = [1, 2, 3, 1, 2, 3, 2, 100, 2, 2, 2]
my_min = my_int_list[0]
for x in my_int_list:
    if x < my_min:
        my_min = x

print("My minimum value is " + str(my_min))

for x in range(5):
    print(f"This is the {x+1}th time I'm running")

# # Exercise multiplication
# my_num = int(input("Enter a number: "))
# for x in range(100):
#     print(f"{my_num} * {x+1} = {my_num * (x+1)}")

# password = ""
# while password != "hello-world-123":
#     password = input("What is the top secret password? ")

# print("You guessed the right password!")

# is_running = True
# while is_running:  # Equivalent to `while is_running is True:`
#     print("This is running")

# To exit an infinite loop, use CTRL + Z or CTRL + C

# guessed_pass = False  # flag variable
# while guessed_pass == False:
#     password = input("What is the top secret password? ")
#     if password == "123":
#         guessed_pass = True

# print("You guessed the right password!")

for x in range(0, 1000):
    if x == 50:
        break
    print("X is ", x)

# Loop forever, increasing y by 1 each time and only breaking out (leaving the loop) when y >= 1000
y = 100
while True:
    print(f"Y is {y}")
    if y >= 1000:
        break
    y += 1

# Loop forever, increasing y by 1 each time
y = 100
while True:
    print(f"Y is {y}")
    if (
        y >= 1000
    ):  # if y >= 1000, then I'm skipping the rest of the loop code and going back to the test condition
        continue
    y += 1  # y = y + 1
