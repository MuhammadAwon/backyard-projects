"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data
"""

import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from feature_format import featureFormat, targetFeatureSplit

dictionary = pickle.load(open("../../resources/enron/dataset_modified_unix.pkl", "rb"))

# list the features you want to look at--first item in the
# list will be the "target" feature
features_list = ["bonus", "salary"]
# features_list = ["bonus", "long_term_incentive"]
data = featureFormat(dictionary, features_list, remove_any_zeroes=True,
                     sort_keys='../../resources/enron/python2_lesson06_keys_unix.pkl')
target, features = targetFeatureSplit(data)

# training-testing split needed in regression, just like classification
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5,
                                                                          random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.

from sklearn.linear_model import LinearRegression

# train regression model
reg = LinearRegression().fit(feature_train, target_train)

# find slope and intercept
print(f'Slope: {reg.coef_}')
print(f'Intercept: {reg.intercept_}')

# score on same training set
print(f'Training score: {reg.score(feature_train, target_train)}')

# score on testing set
print(f'Testing score: {reg.score(feature_test, target_test)}')


# draw the scatterplot, with color-coded training and testing points
for feature, target in zip(feature_test, target_test):
    plt.scatter(feature, target, color=test_color)
for feature, target in zip(feature_train, target_train):
    plt.scatter(feature, target, color=train_color)


# labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")


# draw the regression line, once it's coded
try:
    plt.plot(feature_test, reg.predict(feature_test))
except NameError:
    pass

plt.plot(feature_train, reg.predict(feature_train), color="b")
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
