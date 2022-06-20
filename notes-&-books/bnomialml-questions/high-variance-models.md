# Kendall's interview

Kendall showed up early to her interview.

She was fresh out of her Master's, and this was going to be her first job after school.

After a few pleasantries, the interviewer started talking about high-variance models and how they typically pay a lot of attention to the training data.

Kendall nodded and smiled while imagining the question that was coming. She didn't have to wait longer.

**Which of the following algorithms can be considered high-variance models?**

- [ ] Linear Regression
- [x] Decision Trees
- [ ] Logistic Regression
- [x] k-Nearest Neighbors (KNN)

## Answer

Every machine learning algorithm deals with three types of errors: bias, variance, and irreducible error. We need to focus specifically on the variance error to answer this question.

Here is what **Jason Brownlee** has to say about variance: "Variance is the amount that the estimate of the target function will change if different training data was used."

In other words, variance refers to how much the answers given by the model will change if we use different training data. The model has high variance if the answers differ significantly when using different portions of our training dataset.

Generally, non-linear machine learning algorithms with a lot of flexibility are high variance. For example, Decision Trees and k-Nearest Neighbors are high-variance models. Linear models, on the other hand, are usually low-variance.

## Readings

- ["Gentle Introduction to the Bias-Variance Trade-Off in Machine Learning"](https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/) is Jason Brownlee's article covering bias, variance, and their tradeoff.
- The Wikipedia page on bias and variance is also a good resource: ["Bias–variance tradeoff"](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)
- In case you like the simplicity of Twitter threads, here is one for you about this topic: ["Bias, variance, and their relationship with machine learning algorithms"](https://twitter.com/svpino/status/1390969728504565761)
