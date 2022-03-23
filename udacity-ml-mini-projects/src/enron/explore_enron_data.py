"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).
    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
"""
import pickle


enron_data = pickle.load(open("../../resources/enron/enron_dataset_unix.pkl", "rb"))

# # find data points (people) in the dataset
# print(len(enron_data))


# # find availabe features for each person
# print(len(enron_data['SKILLING JEFFREY K']))


# # find POIs in the dataset
# poi_counter = 0
# for k in enron_data:
#     if enron_data[k]['poi']==1:
#         poi_counter += 1

# print(poi_counter)


# # find POIs in poi_names.txt
# with open('../../resources/enron/poi_names.txt', 'r') as file:
#     data = file.read()

# name_list = data.splitlines()
# print(name_list[2:])
# print(len(name_list[2:]))


# # find total value stock of james prentice
# print(enron_data['PRENTICE JAMES']['total_stock_value'])


# # find email messages from wesley colwell to persons of interest
# print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])


# # find stock value exercised by jeffrey k skilling
# print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])


# # find who took (lay, skilling, and fastow) the most money (total_payments feature)
# print(f"Lay money: {enron_data['LAY KENNETH L']['total_payments']}")
# print(f"Skilling money: {enron_data['SKILLING JEFFREY K']['total_payments']}")
# print(f"Andrew money: {enron_data['FASTOW ANDREW S']['total_payments']}")


# # find people salary and email_address in the dataset
# salary_counter = 0
# email_counter = 0

# for k in enron_data:
#     if enron_data[k]['salary']!='NaN':
#             salary_counter += 1
#     if enron_data[k]['email_address']!='NaN':
#             email_counter += 1

# print(f'People with salary: {salary_counter}')
# print(f'People with email_address: {email_counter}')


# # find number of people with NaN total_payments, and their percentage
# missing_payments_people = 0
# total_people = len(enron_data)

# for k in enron_data:
#     if enron_data[k]['total_payments']=='NaN':
#         missing_payments_people += 1

# pct_missing_payments = missing_payments_people/total_people * 100
# print(f'Missing Payments Percentage: {"%.2f" % pct_missing_payments}')


# # find POIs with nan for their total_payments
# count_nan_payments_ppl=0
# for k in enron_data:
#     if enron_data[k]["poi"]==True:
#         if enron_data[k]['total_payments']=="NaN":
#             count_nan_payments_ppl += 1

# count_poi = 0
# for i in enron_data:
#     if enron_data[i]['poi']==1:
#         counter_poi += 1

# # find percentage
# print(f'Percentage of missing POIs for Payments: {count_nan_payments_ppl/counter_poi*100}')


# # add 10 more persons of interest in the dataset and put nan for their total_payments
# count_total_poi = 0
# for k in enron_data:
#     if enron_data[k]['poi']==True:
#         count_total_poi += 1
#     else:
#         count_total_poi += 1

# # add 10 poi
# ten_poi = 10
# new_total_poi = count_total_poi + ten_poi
# print(f'New no. of people in dataset: {new_total_poi}')

# # find no. of poi with nan for total_payments
# count_nan_total_payments = 0
# for k in enron_data:
#     if enron_data[k]['total_payments']=='NaN':
#         count_nan_total_payments += 1

# # add ten_poi in count_nan_total_payments
# new_missing_payments = count_nan_total_payments + ten_poi
# print(f'NaN for total payments: {new_missing_payments}')


# # find new number of POI's in the new dataset and those POI with NaN for total_payments

# my_enron_data = enron_data
# add_ppl = {'Person1' : {'total_payments': 'NaN', 'poi': True},
#             'Person2' : {'total_payments': 'NaN', 'poi': True},
#             'Person3' : {'total_payments': 'NaN', 'poi': True},
#             'Person4' : {'total_payments': 'NaN', 'poi': True},
#             'Person5' : {'total_payments': 'NaN', 'poi': True},
#             'Person6' : {'total_payments': 'NaN', 'poi': True},
#             'Person7' : {'total_payments': 'NaN', 'poi': True},
#             'Person8' : {'total_payments': 'NaN', 'poi': True},
#             'Person9' : {'total_payments': 'NaN', 'poi': True},
#             'Person10' : {'total_payments': 'NaN', 'poi': True}}

# my_enron_data.update(add_ppl)

# new_poi_ppl = 0
# for k in my_enron_data:
#     if my_enron_data[k]['poi'] == True and my_enron_data[k]['total_payments'] == "NaN":
#         new_poi_ppl += 1

# print(new_poi_ppl)
