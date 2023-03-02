from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    accuracy_score,
    confusion_matrix,
    precision_score,
)
import pandas as pd

df = pd.read_csv("height_weight.csv")

# print(df.info())

# Height into X
X = df["Height"]
# print("---------------------------------------")
# print(X)
X = X.values.reshape(-1, 1)
# print("---------------------------------------")
# print(X)

# Weight into y
y = df.Weight
# print(y)

# lr = LinearRegression()
# reg = lr.fit(X, y)
# print(reg.coef_, reg.intercept_)
# predicted_weight = reg.predict([[140]])

# print(predicted_weight)


# from sklearn.linear_model import LogisticRegression

# height_weight_df = pd.read_csv("height_gender.csv")

# X_hw = height_weight_df.Height.values.reshape(-1, 1)
# y_hw = height_weight_df.Gender

# clf = LogisticRegression()

# result = clf.fit(X_hw, y_hw)
# # print(result)

# y_test = [[145], [148]]
# print(clf.predict_proba(y_test), clf.predict(y_test))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=2000
)

lr = LinearRegression()
reg = lr.fit(X_train.reshape((-1, 1)), y_train)

y_pred = lr.predict(X_test.reshape((-1, 1)))
# print(mean_absolute_error(y_test, y_pred))
# print(mean_squared_error(y_test, y_pred))


# df = pd.read_csv(
#     "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# )

# y = df["species"]
# X = df.drop(
#     ["species"], axis=1
# )  # this function returns a copy of the dataframe with the dropped columns

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.25, random_state=7
# )

# clf = LogisticRegression()
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# acc = accuracy_score(y_test, y_pred)
# print(f"Accuracy is {acc * 100:.2f}%")


# titanic = pd.read_csv(
#     "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
# ).dropna()
# y = titanic["Survived"]
# X = titanic.drop(["Survived"], axis=1)._get_numeric_data()
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
# clf = LogisticRegression()
# clf.fit(X_train, y_train)

# y_pred = clf.predict(X_test)
# print(f"Titanic prediction: {y_pred}")
# tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
# print(f"True positives: {tp}")
# print(f"True negatives: {tn}")
# print(f"False positives: {fp}")
# print(f"False negatives: {fn}")
# print(f"Manual Precision: {tp / (tp + fp)}")
# print(f"Precision: {precision_score(y_test, y_pred)}")


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV

breast_cancer = load_breast_cancer()
hyperparameters = {"C": [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]}

log = LogisticRegression(max_iter=1000)
gs = GridSearchCV(
    log, hyperparameters, cv=5, n_jobs=-1, scoring="accuracy"
)  # 5 folds, using accuracy metric
gs.fit(breast_cancer.data, breast_cancer.target)

print(gs.cv_results_["mean_test_score"])
# array([0.9279615 , 0.94027325, 0.94025772, 0.94904518, 0.95081509, 0.95081509, 0.95433939])

print(gs.cv_results_["rank_test_score"])
# array([7, 5, 6, 4, 2, 2, 1], dtype=int32)

print(gs.best_score_)
