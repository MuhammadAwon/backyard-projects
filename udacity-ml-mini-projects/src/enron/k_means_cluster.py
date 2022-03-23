"""
    Skeleton code for k-means clustering mini-project.
"""

import pickle
import matplotlib.pyplot as plt
from feature_format import featureFormat, targetFeatureSplit


def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    # plot each cluster with a different color--add more colors for
    # drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color=colors[pred[ii]])

    # if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()


# load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load(open("../../resources/enron/enron_dataset_unix.pkl", "rb"))
# there's an outlier--remove it!
data_dict.pop("TOTAL", 0)

# the input features we want to use
# can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = 'total_payments'
poi = "poi"
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list)
poi, finance_features = targetFeatureSplit(data)

# in the "clustering with 3 features" part of the mini-project,
# you'll want to change this line to
# for f1, f2, _ in finance_features:
# (as it's currently written, the line below assumes 2 features)
for f1, f2, _ in finance_features:
    plt.scatter(f1, f2)
# plt.show()

# cluster here; create predictions of the cluster labels
# for the data and store them to a list called pred
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=0).fit(finance_features)
# pred = kmeans.predict(finance_features)

# find min/max of stock and salary features
# max_stock = max(f2 for f1,f2,f3 in finance_features)
# min_stock = min(f2 for f1,f2,f3 in finance_features if f2 != 0)

# max_salary = max(f1 for f1,f2,f3 in finance_features)
# min_salary = min(f1 for f1,f2,f3 in finance_features if f1 != 0)

# print(f'Max Stock: {max_stock}')
# print(f'Min Stock: {min_stock}')

# print(f'Max Salary: {max_salary}')
# print(f'Min Salary: {min_salary}')


# rename the "name" parameter when you change the number of features
# so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="modified_clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("no predictions object named pred found, no clusters to plot")


# compute feature scaling on salary and exercised_stock_options only
import numpy as np
from sklearn.preprocessing import MinMaxScaler

salary_feature = []
stock_feature = []
for name in data_dict:
    sal = data_dict[name]['salary']
    stock = data_dict[name]['salary']
    if sal != 'NaN':
        salary_feature.append(sal)
    if stock != 'NaN':
        stock_feature.append(stock)

salary = np.array([[min(salary_feature)], [200000.0], [max(salary_feature)]])
stock = np.array([[min(stock_feature)], [1000000.0], [max(stock_feature)]])

scaler = MinMaxScaler()
rescaled_salary = scaler.fit_transform(salary)
rescaled_stock = scaler.fit_transform(stock)

print(rescaled_salary)
print(rescaled_stock)
