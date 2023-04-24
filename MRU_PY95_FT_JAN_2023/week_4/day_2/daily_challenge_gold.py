# Prompt user for input
birthday_str = input("What is your birthday? (DD/MM/YYYY): ")

# Split the string using the divider "/" into a list
birthday_list = birthday_str.split("/")

# Assign the day, month and year to variables
birthday_day = int(birthday_list[0])
birthday_month = int(birthday_list[1])
birthday_year = int(birthday_list[2])

# Calculate how many extra candles to add
excess_candles = birthday_year % 10

# Calculate how many extra whitespaces to add due to increased number of candles
# This is done so that the Happy Birthday text remains centered
excess_whitespaces = " " * (excess_candles // 2)

# Account for years that are odd, the uneven whitespace is added to the right
uneven_whitespace = ""
if (excess_candles % 2) == 1:
    uneven_whitespace = " "

# Calculate the total number of candles on the cake
candle_amount = 5 + excess_candles

# Cake line 1 | Candles
cake_str = "       ___iiiii"
for x in range(excess_candles):
    cake_str += "i"
cake_str += "___\n"

# Cake line 2 | Happy text
cake_str += (
    "      |"
    + excess_whitespaces
    + ":H:a:p:p:y:"
    + excess_whitespaces
    + uneven_whitespace
    + "|\n"
)

# Cake line 3 | Layer
# Whitespaces are replaced with layer symbol "_" here
cake_str += (
    "    __|"
    + excess_whitespaces.replace(" ", "_") * 2
    + uneven_whitespace.replace(" ", "_")
    + "___________|__\n"
)

# Cake line 4 | Frosting
# Whitespaces are replaced with frosting symbol "^" here
cake_str += (
    "   |"
    + excess_whitespaces.replace(" ", "^") * 2
    + uneven_whitespace.replace(" ", "^")
    + "^^^^^^^^^^^^^^^^^|\n"
)

# Cake line 5 | Birthday text
cake_str += (
    "   |"
    + excess_whitespaces
    + ":B:i:r:t:h:d:a:y:"
    + excess_whitespaces
    + uneven_whitespace
    + "|\n"
)

# Cake line 6 | Frosting
cake_str += (
    "   |" + excess_whitespaces * 2 + "                 " + uneven_whitespace + "|\n"
)

# Cake line 7 | Base
# Whitespaces are replaced with base symbol "~" here
cake_str += (
    "   ~"
    + excess_whitespaces.replace(" ", "~") * 2
    + uneven_whitespace.replace(" ", "~")
    + "~~~~~~~~~~~~~~~~~~\n"
)

print(cake_str)

# Bonus, leap year means double cake!
if birthday_year % 4 == 0:
    print(cake_str)
