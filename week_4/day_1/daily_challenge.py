user_str = input("Enter a string that is 10 characters long: ")

if len(user_str) < 10:
    print("The string is not long enough")
elif len(user_str) > 10:
    print("The string is too long")
else:
    print(f"The first character is {user_str[0]} and the last is {user_str[-1]}")

    for x in user_str:
        print(x, end="")
    print()

    import random

    # shuffled_string = "".join(random.sample(user_str, len(user_str)))
    # print(shuffled_string)

    shuffled_string = list(user_str)
    random.shuffle(shuffled_string)
    shuffled_string = "".join(shuffled_string)
    print(shuffled_string)
