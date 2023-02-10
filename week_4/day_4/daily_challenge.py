secret_msg = "7i3\n\
    Tsi\n\
    h%x\n\
    i #\n\
    sM \n\
    $a \n\
    #t%\n\
    ^r!"

msg_lines_list = secret_msg.split("\n")
msg_lines_list = [
    line.strip() for line in msg_lines_list
]  # Remove whitespace from both sides

print(f"The lines list contains: {msg_lines_list}")
msg_lines_len_list = [
    len(line) for line in msg_lines_list
]  # Make a list of all line lengths
max_line_len = max(msg_lines_len_list)  # Get the max line length

rotated_msg = ""
for x in range(max_line_len):  # Go through each character from left to right
    for line in msg_lines_list:  # Go through each line from top to bottom
        if x >= len(
            line
        ):  # Prevent overflowing when accessing lines with size less than the max length
            break
        elif line[x].isalpha():  # Add letters to the rotated message
            rotated_msg += line[x]
        else:  # Replace non-letters to whitespaces in rotated message
            rotated_msg += " "

print(f"The raw rotated message is: {rotated_msg}")

# Strip whitespaces
rotated_msg = rotated_msg.strip()
# Remove double whitespaces
while "  " in rotated_msg:
    rotated_msg = rotated_msg.replace("  ", " ")

print(f"The clean rotated message is: {rotated_msg}")
