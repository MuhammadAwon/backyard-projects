import pickle
import numpy
numpy.random.seed(42)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


# The words (features) and authors (labels), already largely processed.
# These files should have been created from the previous (Lesson 10)
# mini-project.
words_file = '../resources/word_data_unix.pkl'
authors_file = '../resources/email_authors_unix.pkl'
word_data = pickle.load(open(words_file, "rb"))
authors = pickle.load(open(authors_file, "rb"))

# test_size is the percentage of events assigned to the test set (the
# remainder go into training)
# feature matrices changed to dense representations for compatibility with
# classifier functions in versions 0.15.2 and earlier
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors,
                                                                                             test_size=0.1,
                                                                                             random_state=42)

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test = vectorizer.transform(features_test).toarray()

# a classic way to overfit is to use a small number
# of data points and a large number of features;
# train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train = labels_train[:150]



### your code goes here
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Make classifier and train on the 
clf = DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)



pred = clf.predict(features_test)
acc = accuracy_score(labels_test, pred)
# print(acc)

important_features = clf.feature_importances_
counter = 0
for feature in important_features:
    if feature > 0.2:
        print(f'Feature: {feature} Index: {counter}')
        break
    counter += 1

print(vectorizer.get_feature_names()[33614])
