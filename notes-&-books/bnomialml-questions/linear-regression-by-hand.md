# Linear regression by hand

The best way to learn something new is to rip the band-aid and tackle a problem from scratch.

Imagine you get a dataset with thousands of samples of houses sold in the U.S. over the last five years. We know the value of a few different features of each home and the price it was sold for. The goal is to build a simple model capable of predicting the price of a new house given those features.

A linear regression model seems like an excellent place to start.

But you are not writing any code yet. You want to do this manually, starting with a matrix `X` containing the value of the features and a vector `w` containing the weights.

The next step is to multiply `X` and `w`, but you aren't sure about the result of this operation.

**Which of the following better describes the result of multiplying `X` and `w`?**

- [ ] The result will be a vector `y` containing the actual price of each house as provided in the dataset.
- [x] The result will be a vector `y` containing the predicted price of each house.
- [ ] The result will be a matrix `y` containing the actual price of each house and the features from the matrix `X`.
- [ ] The result will be a matrix `y` containing the predicted price of each house and the features from the matrix `X`.

## Answer

Let's start by looking at the mathematical properties of the multiplication of a matrix and a vector: Whenever we multiply a `m × n` matrix with a `n × 1` vector, the result will always be a column vector of `m × 1` dimensions.

The third and fourth choices suggest that we'll get a matrix as the result of the operation, but we know the multiplication will return a vector, so we can safely remove them as candidate answers.

The first choice proposes that the result will contain the actual price of each house, while the second choice suggests that the result will be the predicted price. Let's think about this for a moment.

If you look at the multiplication components, we have a matrix containing the features of every house and a vector of weights. The price we are trying to predict isn't part of those features. If you think about it, it won't make sense to predict a price by showing the model that same price (that would be cheating!) The algorithm estimates the vector of weights, so the actual price of the house is not there either.

Looking at the multiplication components, we can conclude that the result is the predicted price. But if you think about the problem logically, you should arrive at the same answer: the entire goal of our model is to predict the price of a house, so that must be the result of the function.

Therefore, the correct choice is the second one: The multiplication result is a vector containing the price predictions.

## References

- [Understanding Linear Regression with Mathematical Insights](https://www.analyticsvidhya.com/blog/2021/08/understanding-linear-regression-with-mathematical-insights/)
- [Linear Regression for Machine Learning](https://machinelearningmastery.com/linear-regression-for-machine-learning/)
