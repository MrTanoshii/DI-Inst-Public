import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 20, 35, 6, 100]
plt.plot(x, y, label='Line oogabooga')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.title('first graph')
plt.show()

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# plt.plot(data.index, data["sepal_length"], "g*") 
# plt.show()

# plt.scatter(data['sepal_length'], data['petal_length'])
# plt.xlabel('sepal_length (centipedes)')
# plt.ylabel('petal_length (centimeters)')
# plt.grid()
# plt.show()


# setosa_data = data[data.species == 'setosa']
# versicolor_data = data[data.species == 'versicolor']
# virginica_data = data[data.species == 'virginica']

# fig, ax=plt.subplots(1,3,figsize=(15, 5))


# ax[0].hist(setosa_data.petal_length, color='g', label = 'setosa')
# ax[1].hist(versicolor_data.petal_length, color='r', label = 'versicolor')
# ax[2].hist(virginica_data.petal_length, color='b', label = 'virginica')

# ax[0].legend()
# ax[1].legend()
# ax[2].legend()
# ax[0].set_ylabel('Frequency')
# ax[1].set_ylabel('Frequency')
# ax[2].set_ylabel('Frequency')
# ax[0].set_xlabel('petal length (cm)')
# ax[1].set_xlabel('petal length (cm)')
# ax[2].set_xlabel('petal length (cm)')
# fig.show()

# # Using NumPy, create an array of length 100 filled with random ints between 0 and 75
# arr_100 = np.random.randint(0, 75, 100)
# print(arr_100)

# # Reshape that array to a 50 x 2 matrix
# arr_50_2 = arr_100.reshape(50, -1)
# print(arr_50_2)

# # Make a scatter plot of the 1st column as the x axis and the second column as the y axis
# plt.scatter(arr_50_2[:, 0], arr_50_2[:, 1])
# plt.show()

# # Now make a histogram of each of the columns and make titles for each plot
# fig, ax = plt.subplots(1, 2, figsize=(15, 5))
# ax[0].hist(arr_50_2[:, 0])
# ax[1].hist(arr_50_2[:, 1])
# ax[0].set_title('First Column')
# ax[1].set_title('Second Column')
# plt.show()

# titanic_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# print(titanic_df.head())


# plt.figure(figsize= (10,5))
# titanic_df.Age.plot(kind="hist")
# plt.xlabel('Age')
# plt.title('Age distribution')
# plt.show()

# titanic_df.groupby('Survived')["Age"].plot(kind='kde', figsize=(10, 5))
# plt.legend()
# plt.title('Age by density by survived')
# plt.show()

# continuous_features = ['SibSp', 'Parch', 'Fare']
# target = 'Survived'
# fig, ax = plt.subplots(3,1,figsize=(8, 8))
# for i, cont_v in enumerate(continuous_features):
#     titanic_df.groupby(target)[cont_v].plot(kind='kde', ax=ax[i])
#     ax[i].set_xlabel(cont_v)
#     ax[i].legend()

# fig.tight_layout()
# plt.show()

# plt.savefig('my_plot_ab_ma_dh_na_sa.png')


# continuous vs discrete

# 0 - 1, continuous | 0.00000045, 0.23529405943, 0.34534636
# 0 - 1, discrete   | 0, 1

# Continuous | Colors, Sex (M/F/L/G/B/T/Q/+), time
# Discrete   | Primary colors, Sex (M/F), car model