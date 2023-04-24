# ----------------------------------------------------------
# Exercise 1
print("Hello world" * 4)

# ----------------------------------------------------------
# Exercise 2
print(f"The result of (99^3)*8 is {((99**3)*8)}")

# ----------------------------------------------------------
# Exercise 3
# 5 < 3                 | False
# 3 == 3                | True
# 3 == "3"              | False
# "3" > 3               | Error
# "Hello" == "hello"    | False

# ----------------------------------------------------------
# Exercise 4
computer_brand = "Lenovo"
print(f"I have a {computer_brand} computer.")

# ----------------------------------------------------------
# Exercise 5
name = "Vincent"
age = 29
shoe_size = 41.5
info = f"Hi, I'm {name}, {age} Python Instructor for Dev Inst. For some reason, you need to know my shoe size which is {shoe_size}"
print(info)

# ----------------------------------------------------------
# Exercise 6
a = 10
b = 12
if a > b:
    print("Hello World")
# ----------------------------------------------------------
# Exercise 7
user_num = int(input("Enter a number: "))
if user_num % 2 == 0:
    print(f"{user_num} is even.")
else:
    print(f"{user_num} is odd.")

# ----------------------------------------------------------
# Exercise 8
user_name = input("Enter your name: ").lower()
if user_name == "vincent":
    print("Dope name bruh")
else:
    print(f"Hi {user_name} (._. )")

# ----------------------------------------------------------
# Exercise 9
user_height_in = float(input("Enter your height in inches: "))
user_height_cm = user_height_in * 2.54

if user_height_cm > 145:
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")
