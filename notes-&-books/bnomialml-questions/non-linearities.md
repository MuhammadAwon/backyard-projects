# Non-linearities

River learned an important lesson when trying to implement a neural network from scratch:

For her network to learn anything useful, she needed to introduce non-linearities.

Whenever she didn't do it, the results were utter trash.

**Which of the following will add non-linearities to River's neural network?**

- [x] Using Rectifier Linear Unit (ReLU) as an activation function.
- [ ] Adding convolution operations to the network.
- [ ] Using Stochastic Gradient Descent to train the network.
- [ ] Implementing the backpropagation process.

## Answer

For a neural network to learn complex patterns, we need to ensure that the network can approximate any function, not only linear ones. This is why we call it "non-linearities."

The way we do this is by using activation functions.

An interesting fact: the **Universal approximation theorem** states that, when using non-linear activation functions, we can turn a two-layer neural network into a universal function approximator. This is an excellent illustration of how powerful neural networks are.

Some of the most popular activation functions are [sigmoid](https://en.wikipedia.org/wiki/Logistic_function), and [ReLU](https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks). Therefore, the first choice is the correct answer to this question.

The second choice is incorrect; a [convolution operation is a linear operation](https://en.wikipedia.org/wiki/Convolution#Properties). You can check [this answer](https://ai.stackexchange.com/questions/19879/arent-all-discrete-convolutions-not-just-2d-linear-transforms) in Stack Exchange for an excellent explanation.

Finally, neither Stochastic Gradient Descent nor backpropagation has anything to do with the linearity of the network operations. Therefore, they aren't correct answers.

## Readings

- Check ["Activation function"](https://en.wikipedia.org/wiki/Activation_function) from Wikipedia to understand more about this topic.
- I find the ["Universal approximation theorem"](https://en.wikipedia.org/wiki/Universal_approximation_theorem) fascinating.
