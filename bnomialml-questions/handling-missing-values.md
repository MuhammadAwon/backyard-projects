# Handling missing values

The customer data the team received was not in great shape.

After some analysis, they found that many values were missing, entire fields were incomplete, and some of the data was corrupted.

Everyone knew they had to fix this before building the machine learning application they had been planning for a year.

The team lead called a special meeting to discuss their next steps, and after some time, they narrowed it down to a few possibilities.

**Which of the following are valid techniques they could use to handle the problems with their data?**

- [x] Replace missing values with the mean, median, mode, or other imputation techniques.
- [x] Drop any rows or columns that contain missing or corrupted data.
- [x] Predict the missing values using a separate machine learning model.
- [x] Using machine learning algorithms that are robust to missing values.

## Answer!

Replacing missing values with the mean, median, mode, or any other imputation techniques are valid approaches to handle this problem. Imputation is very common, and the specific way to go depends on the particular situation. Therefore, the first choice is correct.

Sometimes, a row or column is in such poor shape that the best approach is to drop it altogether. Imagine a column where only a small percentage of rows have value or a column where most of the data is corrupted. In these cases, getting rid of the data may be a good idea. This makes the second choice also correct.

A more advanced technique commonly used is to predict missing values using a separate model. For example, you could use a linear regression model to fill in the blanks on one specific column of data. This approach considers the correlation between other features and the column with missing values, potentially producing good results. This makes the third choice also correct.

Finally, the fourth choice is also correct. We can use a particular implementation of a machine learning algorithm that is robust to missing values. For example, we could run the k-Nearest Neighbors algorithm and ignore a column with missing values when computing the distance. This, however, depends on the implementation of the algorithm, so you need to watch out for that.

In summary, all four choices are correct.

## References
- [How to Handle Missing Data with Python](https://machinelearningmastery.com/handle-missing-data-python/)
- [Imputation of missing values by scikit-learn](https://scikit-learn.org/stable/modules/impute.html#imputation-of-missing-values)
- [Handling Missing Values](https://www.kaggle.com/dansbecker/handling-missing-values)