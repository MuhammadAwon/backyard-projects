# Samples per batch

Gradient Descent is an optimization algorithm frequently used in machine learning applications.

The algorithm can vary in how many data samples we use to calculate the error: a single sample, all available samples, or a batch of samples (more than one but fewer than the entire dataset.)

Naomi read about "Mini-Batch Gradient Descent," and now she is trying to research how it works.

**Which of the following statements is true about Mini-Batch Gradient Descent?**

- [ ] Mini-Batch Gradient Descent uses a single sample of data during every iteration.
- [x] Mini-Batch Gradient Descent uses a batch of data (more than one sample but fewer than the entire dataset) during every iteration.
- [ ] Mini-Batch Gradient Descent uses all of the available data at once during every iteration.
- [ ] Mini-Batch Gradient Descent is an entirely different optimization algorithm, and Trevor shouldn't look at it as something related to Gradient Descent.

## Anwer

Here is a simplified explanation of how [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent) works: We take samples from the training dataset, run them through the model, and determine how far our results are from what we expect. We then use this difference (error) to compute how much we need to update the model weights to improve the results.

A critical decision we need to make is how many samples we use to compute the gradient of the objective function. We have three choices:

- Use a single instance of data.
- Use all of the data at once.
- Use some of the data.

Using a single sample of data is called "Stochastic Gradient Descent" or SGD. Using all the data at once is called "Batch Gradient Descent." Finally, using some of the data—more than one sample but fewer than the entire dataset—is called "Mini-Batch Gradient Descent."

Notice that we always make a tradeoff between the accuracy of the updates and the time it takes to calculate them. While using a single instance of data is faster, the updates will be more inaccurate. On the other hand, using all of the data available while producing more accurate updates requires storing the entire dataset in memory, and it's very slow.

In summary, the second choice is the correct answer to this question.

## Readings

- Check ["An overview of gradient descent optimization algorithms"](https://ruder.io/optimizing-gradient-descent/index.html#gradientdescentvariants) for a deep dive into gradient descent and every one of its variants.
- ["Gradient Descent For Machine Learning"](https://machinelearningmastery.com/gradient-descent-for-machine-learning/) is another great introduction to gradient descent.
- ["A Gentle Introduction to Mini-Batch Gradient Descent and How to Configure Batch Size"](https://machinelearningmastery.com/gentle-introduction-mini-batch-gradient-descent-configure-batch-size/) covers Batch and Mini-Batch Gradient Descent.
