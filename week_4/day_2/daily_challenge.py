# ----------------------------------------------------------
# Challenge 1

num = int(input("Enter a number: "))
multi = int(input("Enter a length of multiples: "))

my_list = []
for x in range(multi):
    my_list.append(num * (x + 1))

print(my_list)

# ----------------------------------------------------------
# Challenge 2

user_text = input("Enter a string: ")

sanitized_str = ""
for x in range(len(user_text)):
    is_valid = True
    for y in range(x + 1, len(user_text)):
        if user_text[x] == user_text[y]:
            # Make character invalid if the next is the same
            is_valid = False
            break
        else:
            # The character is valid if the next is different
            break
    if is_valid:
        sanitized_str += user_text[x]

print(sanitized_str)
