import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
# pickle is used to save a model, every time this project is run it retrains
# the model saving it in this case means we can save the most accurate model
# but in larger projects it can take hours to learn from the data so saving
# it will save many hours
import pickle
from matplotlib import style

# there is a separator because each person is one long
# line of words and numbers
data = pd.read_csv('student-mat.csv', sep=";")

# makes data only display certain columns
data = data[["G1", "G2", 'G3', 'studytime', 'failures', 'absences']]

# the data we want to predict is known as a label
# in the spreadsheet G3 is their final score
predict = 'G3'

# drop will return a new data frame without G3 and that will be the training
# data that will try and predict what G3 is
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

# this takes all of the attributes and splits them into four different arrays
# x_train takes a sections of the data from X and y_train does the same thing
# with y
# x_test and y_test are used to test the accuracy of the model
# if the model was trained of all the data it would memorise it and would
# already know what the answer would be. train_test_split takes a three
# arguments: set of data that we want to know, set of data we know, amount of
# data used to teach the model=float
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

# this is commented because the model has been saved
"""linear = linear_model.LinearRegression()

# this fits the data to find the best fit line
linear.fit(x_train, y_train)

# returns the accuracy
acc = linear.score(x_test, y_test)

print(acc)

# save as pickle
with open("studentmodel.pickle", 'wb') as f:
    pickle.dump(linear, f)"""

pickle_in = open("studentmodel.pickle", 'rb')

# loads the pickle file
linear = pickle.load(pickle_in)

acc = linear.score(x_test, y_test)

print(acc)

print('Coefficient: \n', linear.coef_)
print("Intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
