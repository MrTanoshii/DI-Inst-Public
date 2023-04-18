user_input = input("Enter a sentence: ")
user_input = user_input.split(" ")

# # First method
# user_input.reverse()
# reverse_input = user_input

# Second method
reverse_input = []
for x in range(len(user_input) - 1, -1, -1):
    reverse_input.append(user_input[x])


print(reverse_input)
