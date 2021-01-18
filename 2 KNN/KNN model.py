import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

# even though it isn't a csv file it can still be read as one
# due to the way it is written
data = pd.read_csv("car.data")
print(data.head())

# as 2 KNN does computations with the data it is necessary that
# the data is in numerical form
# so this converts it
# le takes the labels and encodes them into appropriate
# integers
le = preprocessing.LabelEncoder()
# the line below gets the entire buying column, turns
# it into a list and converts in into numerical values
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

# the parameter is the amount of neighbours
model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train, y_train)


predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "very good"]

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]],
          "Data: ", x_test[x], "Actual: ", names[y_test[x]])
    n = model.kneighbors([x_test[x]], 9, True)
    print("N: ", n)


acc = model.score(x_test, y_test)
print(acc)