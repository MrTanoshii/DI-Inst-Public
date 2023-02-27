import numpy as np

numbers = [1, 2, 3, 4, 5, 6, 10]
numpy_arr = np.array(numbers)


# print(numpy_arr)

# # Multiply all the values of numbers by 2

# # Python way
# # numbers *= 2  # This does not work
# # numbers = numbers * 2

# print(numbers)
# numbers_times_2 = []

# for number in numbers:
#     x = number * 2
#     numbers_times_2.append(x)

# print(numbers_times_2)

# numbers_times_2 = [number * 2 for number in numbers]
# print(numbers_times_2)

# # NumPy way
# print(numpy_arr * 2)

# Add 5 to all values of numbers
# numbers_add_2 = [number + 2 for number in numbers]
# print(numbers_add_2)

# print(numpy_arr + 2)

# tic_tac_toe = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


numpy_arr_2d = np.arange(50)
print(numpy_arr_2d)

numpy_arr_2d = numpy_arr_2d.reshape((2, 25))
print(numpy_arr_2d)
print(numpy_arr_2d.shape)

# numpy_arr_2d = numpy_arr_2d.reshape((10, 5))
# print(numpy_arr_2d)
# print(numpy_arr_2d.shape)

# numpy_arr_3d = numpy_arr_2d.reshape((5, 2, 5))
# print(numpy_arr_3d)
# print(numpy_arr_3d.shape)
# print(numpy_arr_3d - 10)

# numpy_arr_2d = numpy_arr_2d.reshape((-1, 5)) # -1 to tell numpy to calculate the value by itselfs
# print(numpy_arr_2d)
# print(numpy_arr_2d.shape)

# print(numpy_arr_2d[1, :])

# print(numpy_arr_2d.mean())
# print(numpy_arr_2d.max())
# print(np.median(numpy_arr_2d))
# print(np.std(numpy_arr_2d))


def arr_1d_proc(arr_1d):
    minimum_value = arr_1d.min()
    standard_deviation = arr_1d.std()
    product = np.prod(arr_1d)
    dot_product = np.dot(arr_1d, arr_1d)
    arr_1d_minus_4 = arr_1d - 4
    return minimum_value, standard_deviation, product, dot_product, arr_1d_minus_4


result = arr_1d_proc(np.arange(10))
print(result)
