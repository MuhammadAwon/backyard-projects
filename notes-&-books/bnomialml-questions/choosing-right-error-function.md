# Patricia is building a logistic classifier

Patricia has been working on a logistic classifier for a new project.

She knows that the key to getting successful predictions depends on the error function she decides to use. She wants this function to have the following characteristics:

- The function should return a small number if the sample is correctly classified.
- The function should return a large number if the sample is incorrectly classified.
- The error for a set of samples should be the sum or average of the errors for all the samples.

Patricia has several choices but would like to hear your opinion.

**Which of the following would be the best error function for a logistic classifier?**

- [ ] Absolute error: a function that returns the absolute value of the difference between the prediction and the label.
- [ ] Square error: a function that returns the square of the difference between the prediction and the label.
- [x] Log loss: a function that returns the negative logarithm of the product of probabilities.
- [ ] Mean percentage: a function that returns the average error of the differences between predicted and actual values.

## Answer

Out of the four choices in this question, the first three error functions satisfy Patricia's three characteristics. The absolute error, the square error, and the log loss are good choices based on this. The "mean percentage" is a made-up error function that we threw in there for fun, so we can quickly discard it as a valid answer.

Now, out of the three functions that satisfy Patricia's requirements, we need to analyze whether they can be used to build a binary classification model.

Neither the absolute nor square error functions are used in binary classification problems. They don't penalize mistakes as harshly as log loss does, so they aren't a good choice for this type of problem.

Log loss, however, is one of the most popular error functions and a perfect fit for a binary classifier like the one Patricia is trying to build. Therefore, the third choice is the correct answer.

## References

- [Logistic Regression for Machine Learning](https://machinelearningmastery.com/logistic-regression-for-machine-learning/)
- [Logistic Regression: Loss and Regularization](https://developers.google.com/machine-learning/crash-course/logistic-regression/model-training)
- [Logistic Regression](https://web.stanford.edu/~jurafsky/slp3/5.pdf)