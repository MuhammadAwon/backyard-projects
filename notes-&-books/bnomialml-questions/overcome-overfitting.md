# Claudia needed a walk

After hours of work, Claudia decided to take a break.

She has been working on a model to classify music into different genres, and while her neural network is doing great during training, its accuracy struggles with the test data.

Claudia took a walk and came back with a fresh perspective. She wrote down a few strategies to approach the problem.

**Which of Claudia's strategies would you say is likely to help her solve the issue?**

- [x] Decrease the complexity of the model by cutting down layers and reducing the number of neurons.
- [ ] Switch to a different optimization algorithm.
- [x] Regularize the model.
- [x] Increase the amount of training data.

## Answer

Claudia's model is overfitting.

Her model is doing great with the training data but struggling on the test set, which is a sign that her model is not generalizing well to unseen samples.

If Claudia decreases the complexity of the model, she could prevent the neural network from "memorizing" the training samples. Complex models tend to overfit because they have too much capacity. It's easier for them to memorize the training data instead of trying to generalize. Therefore, the first choice is a valid strategy to solve the problem.

Switching the optimization algorithm is unlikely to solve this problem. Nothing in the statement gives us any information about which algorithm Claudia is currently using, and we don't have any reason to believe it's not a good one. We also know that her model is learning the training data, which wouldn't be possible if the optimization algorithm wasn't appropriate.

Claudia could also use regularization techniques to help with overfitting. Regularization discourages the model from becoming too complex or flexible, which helps prevent the model from "memorizing" the training data.

Finally, there's a chance that the training data that Claudia is using doesn't fully capture the breadth of valid samples for her problem. In other words, her training dataset might not be enough to teach the model how to predict the test data correctly. In this case, adding more data to the training set gives Claudia a better chance to build a model that generalizes better.

The first, third, and fourth choices are good strategies to solve Claudia's problem.

## Readings

- Check ["Overfitting and Underfitting With Machine Learning Algorithms"](https://machinelearningmastery.com/overfitting-and-underfitting-with-machine-learning-algorithms/) for an introduction to overfitting and underfitting in machine learning.
- ["How to Solve Underfitting and Overfitting Data Models"](https://allcloud.io/blog/how-to-solve-underfitting-and-overfitting-data-models/) covers several strategies to solve overfitting and underfitting.
