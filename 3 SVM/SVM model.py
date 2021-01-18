import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_breast_cancer()

# print(cancer.feature_names)
# print(cancer.target_names)

X = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

# don't ask why this is here, it's not used
classes = ['malignant' 'benign']

# svc stands for support vector classifications
# it takes many different parameters but doesn't have to take
# any
# C=amount of points allowed in the margin
# KNN is also a viable algorithm for this even though it
# usually struggles on multi-dimensional datasets with many
# attributes (this one has around 30) although SVM is better
# in general
# clf = KNeighborsClassifier(n_neighbors=9)
clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)

print(acc)
