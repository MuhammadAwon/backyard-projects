"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.
    Use a Naive Bayes Classifier to identify emails by their authors
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
from time import time
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# create naive bayes classifier
nb_clf = GaussianNB()

# train the classifier
time_fit = time()
nb_clf.fit(features_train, labels_train)
print(f'Training time: {round(time()-time_fit,3)} sec')

# make predictions
time_pred = time()
nb_pred = nb_clf.predict(features_test)
print(f'Prediction time: {round(time()-time_pred, 3)} sec')

# find accuracy
nb_acc = accuracy_score(labels_test, nb_pred)
print(f'Accuracy: {"%.2f" % nb_acc}')
#########################################################


