"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.
    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
from time import time
from numpy.lib.function_base import disp
from sklearn import svm
from sklearn.metrics import accuracy_score
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

# create svm classifier
svm_clf = svm.SVC(kernel='rbf', C=10000.)

# # smaller training dataset
# features_train = features_train[: len(features_train)//100]
# labels_train = labels_train[: len(labels_train)//100]

# train the classifier
time_fit = time()
svm_clf.fit(features_train, labels_train)
print(f'Training time: {round(time()-time_fit, 3)} sec')

# make predicitions
time_pred = time()
svm_pred = svm_clf.predict(features_test)
print(f'Prediction time: {round(time()-time_pred, 3)} sec')

# find accuracy
svm_acc = accuracy_score(labels_test, svm_pred)
print(f'Accuracy: {"%.2f" % svm_acc}')

# # find the class for element 10
# answer = svm_pred[10]
# print(f'Class for element 10: {answer}')

# # find the class for element 26
# answer2 = svm_pred[26]
# print(f'Class for element 26: {answer2}')

# # find the class for element 50
# answer3 = svm_pred[50]
# print(f'Class for element 50: {answer}')

# find the correctly classified labels using confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, svm_pred)
print(f'Confusion matrix: {cm}')
#########################################################



