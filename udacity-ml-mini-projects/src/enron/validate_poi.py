"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../../resources/enron/enron_dataset_unix.pkl", "rb"))

# first element is our labels, any added elements are predictor
# features. Keep this the same for the mini-project, but you'll
# have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys='../../resources/enron/python2_lesson13_keys_unix.pkl')
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# make DT classifier
dt_clf = DecisionTreeClassifier()

# # USE WHOLE DATA FOR ACCURACY
# # fit the model
# dt_clf = dt_clf.fit(features, labels)

# # make predictions on same data that is used for training the model
# pred = dt_clf.predict(features)

# # find accuracy
# acc = accuracy_score(labels, pred)
# print(f"Accuracy on all data: {'%.3f' % acc}")

# split the data into training and test sets with 30% for test data and random_state to 42
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.30, random_state=42)

# fit the model on training set
dt_clf = dt_clf.fit(train_features, train_labels)

# make predictions on test features
pred = dt_clf.predict(test_features)

# find accuracy on test labels
acc = accuracy_score(test_labels, pred)

print(f'Accuracy on test set: {"%.3f" % acc}')
