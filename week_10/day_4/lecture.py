# data_list = [1, 2, 3, 4]

# print(f"Original List: {data_list}")

# # data_index_list = [data_list[0], data_list[1], data_list[2], data_list[3]]

# temp_value = data_list[1]
# data_list[1] = data_list[2]  # Replace 2 by 3
# # data_list[2] = data_list[1] # Replace 3 by 3
# data_list[2] = temp_value

# print(f"Modified List: {data_list}")

# data_list[1], data_list[2] = data_list[2], data_list[1]

# print(f"Modified List: {data_list}")


# actual_list =  data_list

from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"Time <{func.__name__}>: {end-start}")

    return wrapper


@timer
def function_to_measure(arg1, arg2, step=1):
    for i in range(arg1, arg2, step):
        useless_var = i * i**i


function_to_measure(1, 1000, 5)
