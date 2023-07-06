import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# print(df)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.describe())

# print(df['sepal_length'])
# print(df[['sepal_length', 'petal_width']])
# print(df[['sepal_length', 'petal_width', 'species']])

#        [15, 30, 50, 23]
# Index    0,  1,  2,  3
# Position 1,  2,  3,  4

#        [15, 30, 23]
# Index    0,  1,  2
# Position 1,  2,  4

# print(df.iloc[2])
# print(df.loc[2]) # Vincent, do this

# # print(df['sepal_length'])
# print(df.sepal_length.unique())

# print(df.species.unique())

# print(df.sepal_length == 4.7)

# # print(df.sort_values('sepal_length', ascending=True))
# # sorted_df = df.sort_values('sepal_length', ascending=True)
# sorted_df = df.sort_values('sepal_length', ascending=False)
# print(sorted_df.head())
# print(sorted_df.iloc[2])
# print(sorted_df.loc[2])

# print(df.groupby('species').apply(np.mean))

# Use df Vincent
# print(df)
# print(df.loc[(((((((((((((((((((((((((49)))))))))))))))))))))))))])

# - Get the 50th to 60th row of the Iris DataFrame skipping 
# every other row and return a new DataFrame of just
# the species, petal_length, and petal_width

# result = df.loc[49:59:2][['species', 'petal_length', 'petal_width']]
# print(result)


# - Group the data by species and 
# 
# get the median of sepal_length for each group
# and
# get the sum of sepal_length for each group

# df[["species", "sepal_length"]].groupby('species').apply(np.sum)
# df[["species", "sepal_length"]].groupby('species').apply(np.median)


result = (
    df[["species", "sepal_length"]]
    .groupby("species")
    .agg(np.mean)
    .rename({"sepal_length": "mean"}, axis=1)
    .join(
        df[["species", "sepal_length"]]
        .groupby("species")
        .agg(np.sum)
        .rename({"sepal_length": "sum"}, axis=1)
    )
)
print(result)
