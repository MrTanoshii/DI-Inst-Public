import matplotlib.pyplot as plt
import scipy
import pandas as pd
import numpy as np

# x = [1, 2, 3, 4]
# y = [2, 20, 35, 6]
# z = [10, 20, 30, 40]
# fig = plt.figure()
# ax = plt.axes(projection="3d")
# ax.plot3D(x, y, z, "gray")

# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("first graph")
# plt.legend("hello")
# plt.show()

# plt.show()
# plt.show()
# plt.show()
# plt.show()

# data = pd.read_csv(
#     "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# )
# plt.plot(data.index, data["sepal_length"], "g--")
# plt.show()


# plt.scatter(data["sepal_length"], data["petal_length"])
# plt.xlabel("sepal_length (cm)")
# plt.ylabel("petal_length (cm)")
# plt.grid()
# plt.show()

# setosa_data = data[data.species == "setosa"]
# versicolor_data = data[data.species == "versicolor"]
# virginica_data = data[data.species == "virginica"]

# fig, ax = plt.subplots(1, 3, figsize=(13, 5))


# ax[0].hist(setosa_data.petal_length, color="g", label="setosa")
# ax[1].hist(versicolor_data.petal_length, color="r", label="versicolor")
# ax[2].hist(virginica_data.petal_length, color="b", label="virginica")

# ax[0].legend()
# # ax[1].legend()
# ax[2].legend()
# ax[0].set_ylabel("Frequency")
# ax[1].set_ylabel("Frequency")
# ax[2].set_ylabel("Frequency")
# ax[0].set_xlabel("petal length (cm)")
# ax[1].set_xlabel("petal length (cm)")
# ax[2].set_xlabel("petal length (cm)")

# plt.show()


# # Exercise
# random_arr = np.random.randint(0, 75, 100)
# print(random_arr)

# reshaped_arr = random_arr.reshape(50, 2)
# print(reshaped_arr)

# x_data = reshaped_arr[:, 0]
# print(x_data)

# y_data = reshaped_arr[:, 1]
# print(y_data)

# fig, ax = plt.subplots(1, 3, figsize=(13, 5))
# ax[0].scatter(x_data, y_data)
# ax[1].hist(x_data)
# ax[2].hist(y_data)

# plt.show()

titanic_df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)
print(titanic_df.head())

# male_data = titanic_df[titanic_df.Sex == "male"].Survived.value_counts(normalize=True)
# female_data = titanic_df[titanic_df.Sex == "female"].Survived.value_counts(
#     normalize=True
# )

# fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# ax[0].pie(
#     male_data,
#     labels=male_data.index.map({0: "Drown", 1: "Survived"}),
#     autopct="%1.3f%%",
# )
# ax[0].set_title("Male Passengers")

# ax[1].pie(
#     female_data,
#     labels=male_data.index.map({0: "Perished", 1: "Survived"}),
#     autopct="%1.1f%%",
# )
# ax[1].set_title("Female Passengers")

# plt.show()


# plt.figure(figsize=(10, 5))
# titanic_df.Age.plot(kind="hist")
# plt.xlabel("Age")
# plt.title("Age distribution")
# plt.show()

# titanic_df.groupby("Survived")["Age"].plot(kind="kde", figsize=(10, 5))
# plt.legend()
# plt.title("Age by density by survived")
# plt.show()

# continuous_features = ["SibSp", "Parch", "Fare"]
# target = "Survived"
# fig, ax = plt.subplots(3, 1, figsize=(8, 8))
# for i, cont_v in enumerate(continuous_features):
#     titanic_df.groupby(target)[cont_v].plot(kind="kde", ax=ax[i])
#     ax[i].set_xlabel(cont_v)
#     ax[i].legend()

# fig.tight_layout()
# plt.show()

# Exercise

# plt.hist(titanic_df["Fare"], color="Green")
# plt.xlabel("SLKDJFLKDSHFLKJDS")
# plt.title("Ra'ees")
# plt.show()

p_classes = titanic_df.Pclass.unique()
print(p_classes)
colours = {"Not Survived": "k", "Survived": "b"}

fig, ax = plt.subplots(1, len(p_classes), figsize=(14, 8))
for index, column in enumerate(p_classes):
    data = titanic_df[titanic_df.Pclass == column].Survived.value_counts(normalize=True)
    labels = data.index.map({0: "Not Survived", 1: "Survived"})
    ax[index].pie(
        data,
        labels=labels,
        autopct="%1.2f%%",
        colors=[colours[key] for key in labels],
    )
    print(data.index.map({0: "Not Survived", 1: "Survived"}))
    print([(key, colours[key]) for key in labels])
    print("-----")
    ax[index].title.set_text(f"Pclass: {column}")


plt.suptitle("Survival rate grouped by PClass")
plt.show()
