import numpy as np

# # Conversion from Python list to Numpy Array
# lst = [2, 4, 6, 8, 13, 2020]
# print(lst)
# print(type(lst))

# numpy_arr = np.array(lst)
# print(numpy_arr)
# print(type(numpy_arr))

# lst_2d = [[3, 5, 7, -4, 1], [0, 5, 33, -750, 2]]
# numpy_arr_2d = np.array(lst_2d)
# print(numpy_arr_2d)
# print(type(numpy_arr_2d))

# # Numpy array shape & reshaping
# print(numpy_arr.shape)
# print(numpy_arr_2d.shape)

# numpy_arr_reshaped = numpy_arr.reshape((3,2))
# print(numpy_arr_reshaped)
# print(numpy_arr_reshaped.shape)

# numpy_arr_reshaped = numpy_arr.reshape((2,3))
# print(numpy_arr_reshaped)
# print(numpy_arr_reshaped.shape)

# numpy_arr_reshaped = numpy_arr.reshape((1,6))
# print(numpy_arr_reshaped)
# print(numpy_arr_reshaped.shape)

# numpy_arr_reshaped = numpy_arr.reshape((3,-1))
# print(numpy_arr_reshaped)
# print(numpy_arr_reshaped.shape)


# lst_10 = [2, 4, 6, 8, 13, 2020, 4, 6, 8, 13]
# numpy_arr_10 = np.array(lst_10)
# numpy_arr_reshaped = numpy_arr_10.reshape((-1, 2))
# print(numpy_arr_reshaped)
# print(numpy_arr_reshaped.shape)

# # Indexing and slicing
# print(numpy_arr_10[4])
# print(numpy_arr_10[-4:-2])
# print(numpy_arr_10[-6:-2:2])

# print("2D array slicing")
# # lst_2d = [[3, 5, 7, -4, 1], [0, 5, 33, -750, 2]]
# print(numpy_arr_2d[:, 1])
# print(numpy_arr_2d[:, 2])

# # Statistical & maths methods
# print(np.mean(numpy_arr_2d))
# print(np.median(numpy_arr_2d))
# print(np.min(numpy_arr_2d))
# print(np.max(numpy_arr_2d))
# print("Add 10")
# print(numpy_arr_2d + 10)
# print("Minus 10")
# print(numpy_arr_2d - 10)
# print("Times 10")
# print(numpy_arr_2d * 10)
# print("Divide by 10")
# print(numpy_arr_2d / 10)
# print("Power 10")
# print(numpy_arr_2d ** 10)

# py_list = [10, 20, 30]
# print(py_list * 3)

# # Generating a range of values
# for x in range(0, 10):
#     print(x)

# array_range = np.arange(100000000).reshape((25, -1))
# print(array_range)
# print(array_range.shape)
# print(f"The mean value is: {np.mean(array_range)}")

# # NaN and Inf
# array_range = array_range / 0
# print(array_range)

# Exercise
arr_safidy = [3, 11, 19, 21, 23, 30]
nparr_melanie = np.array(arr_safidy)

def fn_naiza(np_arr):
    xxvxccxbcvb = np.min(np_arr) # dummy name, please don't do this
    res_std = np.std(np_arr)
    res_prd = np_arr * np_arr
    res_dot = np.dot(np_arr, np_arr)
    
    # Packing into a tuple
    return xxvxccxbcvb, res_std, res_prd, res_dot

result = fn_naiza(nparr_melanie)
print(result)

# Unpacking a tuple into variables
(result_min, result_std, result_prd, result_dot) = result
print(result_min, result_std, result_prd, result_dot)
