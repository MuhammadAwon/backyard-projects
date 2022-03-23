"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.
    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
from time import time
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

# create dt classifier
dt_clf = DecisionTreeClassifier(min_samples_split=40)

# train the model
t0 = time()
dt_clf.fit(features_train, labels_train)
print(f'Training time: {round(time()-t0, 3)}sec')

# make predictions
t1 = time()
dt_pred = dt_clf.predict(features_test)
print(f'Prediction time: {round(time()-t1, 3)}sec')

# find accuracy
dt_acc = accuracy_score(labels_test, dt_pred)
print(f'Accuracy: {"%.2f" % dt_acc}')

#########################################################
