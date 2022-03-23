import pickle
from typing import Iterator
import matplotlib.pyplot as plt
from feature_format import featureFormat, targetFeatureSplit

# read in data dictionary, convert to numpy array
data_dict = pickle.load(open('../../resources/enron/enron_dataset_unix.pkl', "rb"))
features = ["salary", "bonus"]

# remove the outlier (TOTAL) from the data_dict
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)


### your code below

# # visualize the data for outliers
# for point in data:
#     salary = point[0]
#     bonus = point[1]
#     plt.scatter(salary, bonus)

# plt.xlabel('salary')
# plt.ylabel('bonus')
# plt.show()


# # find the largest outlier (i.e. person with maximum bonus, Which is mistakenly "TOTAL")
# for k in data_dict:
#     if data_dict[k]['bonus']==data.max():
#         print(k)


# # find 2 outliers that have at least 5M bonuses and over 1M salary
# outlier_ppl = []
# for k in data_dict:
#     sal_val = data_dict[k]['salary']
#     bon_val = data_dict[k]['bonus']
#     if sal_val != "NaN" and bon_val != "NaN":
#         outlier_ppl.append((k, int(sal_val), int(bon_val)))

# outliers_salary = 1000000
# outliers_bonuses = 5000000
# for name in outlier_ppl:
#     if name[1] > outliers_salary and name[2] >= outliers_bonuses:
#         print(name)


