# Accuracy as a loss function

Luna knows that the entire goal of gradient descent is to minimize the value of a function. The lower its value, the better the model will be. She has been thinking about designing a custom loss function for her use case.

She wants to use the inverse of the model's accuracy as the loss function. This way, the model will try to minimize the number of mistakes it makes by looking directly at the accuracy of the predictions.

Unfortunately, she soon discovers that this doesn't work.

**What is the problem with this approach?**

- [x] Accuracy is not a differentiable function, so it can't be optimized using gradient descent.
- [ ] Luna wants to optimize for high accuracy but gradient descent is a minimization algorithm; the opposite of what she needs.
- [ ] Minimizing the inverse of the accuracy is a very slow process because of the extra computations needed to compute the final value.
- [ ] Gradient descent only works with a predefined set of loss functions.

## Answer

We use loss functions to optimize a model. We use accuracy to measure the performance of that model.

Usually, we can see how the accuracy of a classification model increases as the loss decreases. This is not always the case, however. The loss and the accuracy measure two different aspects of a model. Two models with the same accuracy may have different losses.

An important insight: The loss function must be continuous, but accuracy is discrete. When training a neural network with gradient descent, we need a differentiable function because the algorithm can't optimize non-differentiable functions. One of the required characteristics for a function to be differentiable is that it must be continuous. Since accuracy isn't, we can't use it.

This makes the first choice the correct answer to this question.

The second and third choices assume that we can use accuracy as the loss function one way or the other, so they are incorrect. The fourth choice claims that gradient descent can only work with a predefined subset of functions, which is also wrong.

## Readings

- ["Loss and Loss Functions for Training Deep Learning Neural Networks"](https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/) is a great introduction to loss functions.
- Check ["How to Choose Loss Functions When Training Deep Learning Neural Networks"](https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/) for a guide on how to choose and implement different loss functions.