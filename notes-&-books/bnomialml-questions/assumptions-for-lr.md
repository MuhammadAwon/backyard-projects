# Reese's baseline

Starting with a simple baseline is a great way to approach a new problem.

Reese knew that, and her go-to has always been a simple Linear Regression, probably one of the most popular algorithms in statistics and machine learning.

But Reese knows that for Linear Regression to work, she must consider several assumptions about the problem.

**Which of the following are some of the assumptions that Reese should make for Linear Regression to be a good candidate for her baseline?**

- [x] The relationship between the features in the data and the target variable must be linear.
- [ ] The features in the data are highly correlated between them.
- [x] The features in the data and the target variable are not noisy.
- [ ] There must not be more than two relevant features plus the target variable.

## Answer

Perhaps evident, for linear regression to work, we need to ensure that the relationship between the features and the target variable is linear. If it isn't, linear regression won't give us good predictions.

Sometimes, this condition means we have to transform the input features before using linear regression. For example, if you have a variable with an exponential relationship with the target variable, you can use log transform to turn the relationship linear. Therefore, the first choice is one correct answer to this question.

The second choice argues that features should be highly correlated, but the opposite is true in reality. Linear regression will overfit your data when you have highly correlated features. Therefore, the second choice is incorrect.

Linear regression requires that your features and target variables are not noisy, so the third choice is also correct. The less noise in your data, the better predictions you'll get from the model. Here is Jason Brownlee in *"Linear Regression for Machine Learning"*:

> Linear regression assumes that your input and output variables are not noisy. Consider using data cleaning operations that let you better expose and clarify the signal in your data.

Finally, there's no technical limitation on how many features we can use when using linear regression. The *Curse of Dimensionality* tells us that as we increase the dimensionality of our data, we will need more samples, but there's no such thing as a limited number of features. Therefore, the fourth choice is not correct.

In summary, the first and third choices are correct.

## References

- [Linear Regression for Machine Learning](https://machinelearningmastery.com/linear-regression-for-machine-learning/)
- [Linear Regression Assumptions](https://en.wikipedia.org/wiki/Linear_regression#Assumptions)
- [Curse of Dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality)
