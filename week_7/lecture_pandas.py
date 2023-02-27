import pandas as pd
import numpy as np

df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
)
# print(df.head())
# print(df)
# print(df.shape)
# print(df.info)
# print(df.describe())
# print(df["petal_length"])
# print(df[["species", "petal_length", "sepal_width"]][df.species == "virginica"])
# print(
#     df.groupby("species").agg(np.sum)
# )  # Instead of apply(), consider transform() or agg()
# print(df.species.unique())
# print(df.sort_index(ascending=False))

# print(df.sort_values("sepal_length", ascending=False))

# Exercise

# print(df.loc[50])
# print(df.iloc[50])

# print(df.loc[50:60:2][["species", "petal_length", "petal_width"]])

print(df.groupby("species").agg(np.median)["sepal_length"])

print(df.groupby("species").agg(np.sum)["sepal_length"])

result = (
    df[["species", "sepal_length"]]
    .groupby("species")
    .agg(np.median)
    .rename({"sepal_length": "mean"}, axis=1)
    .join(
        df[["species", "sepal_length"]]
        .groupby("species")
        .agg(np.sum)
        .rename({"sepal_length": "sum"}, axis=1)
    )
)

print(result)
