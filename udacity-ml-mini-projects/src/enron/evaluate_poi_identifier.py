"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
from sklearn.model_selection import train_test_split
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../../resources/enron/enron_dataset_unix.pkl", "rb"))

# add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

data = featureFormat(data_dict, features_list, sort_keys='../../resources/enron/python2_lesson14_keys_unix.pkl')
labels, features = targetFeatureSplit(data)

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score

# make DT classifier
dt_clf = DecisionTreeClassifier()

# fit the model on training set
dt_clf = dt_clf.fit(X_train, y_train)

# make predictions
pred = dt_clf.predict(X_test)


# # find the number of POI in the test set
# poi_in_test = [i for i in y_test if i==1]
# print(len(poi_in_test))

# # find the total number of people in the test set
# print(len(X_test))

# # find the true positives if there are any (the case where both actual and predicted label are 1)
# identify_tp = classification_report(y_test, pred)
# print(identify_tp)

# # find the precision of POI identifier
# precision = precision_score(y_test, pred)
# print(precision)

# # find the recall of POI identifier
# recall = recall_score(y_test, pred)
# print(recall)

## fabricated data just to get some practice on confusion mattrix, precision, and recall concepts
# predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
# true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

# # find TP, TN, FP, FN
# print(confusion_matrix(true_labels, predictions))

# tp = 6
# tn = 9
# fp = 3
# fn = 2

# # find precision
# find_precision = tp / (tp+fp)
# print(find_precision)

# # find recall
# find_recall = tp / (tp+fn)
# print(find_recall)

# # find precision and recall using sklearn functions
# pre = precision_score(true_labels, predictions)
# re = recall_score(true_labels, predictions)
# print(pre)
# print(re)