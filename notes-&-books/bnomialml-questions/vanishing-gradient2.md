# Harper and the small gradients

Harper's team is struggling with the deep neural network they have been building.

Unfortunately, during backpropagation, the gradient values of their network decrease dramatically as the process gets closer to the initial layers, preventing them from learning at the same pace as the last set of layers.

Harper knows their model suffers from the vanishing gradient problem. She decides to research every possible option to improve their model.

**Which of the following techniques will make Harper's model more robust to the vanishing gradient problem?**

- [x] Harper should try ReLU as the activation function since it's well-known for mitigating the vanishing gradient problem.
- [x] Harper should modify the model architecture to introduce Batch Normalization.
- [x] Harper should make sure they are initializing the weights properly. For example, using He initialization should help with the vanishing gradient problem.
- [ ] Harper should increase the learning rate to avoid getting stuck in local minima and thus reduce the chance of suffering vanishing gradients.

## Answer

If the gradients of the loss function approach zero, the model will stop learning because the network will stop updating the weights. This phenomenon is known as the [Vanishing Gradient Problem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem), and it's very common when using the [Sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function) and [Tanh](https://www.sciencedirect.com/topics/mathematics/hyperbolic-tangent-function) activation functions in deep neural networks.

In contrast, [ReLU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) is a way to solve the vanishing gradient problem. ReLU is much less likely to saturate, and its derivative is `1` for values larger than zero.

[Batch normalization](https://en.wikipedia.org/wiki/Batch_normalization) is another way to mitigate the vanishing gradient problem. Suppose we have a layer that uses a Sigmoid activation function. We can normalize the input to that layer to ensure that the values don't reach the edges and stay around the area where derivatives aren't too small. By modifying the input to this layer with batch normalization, we will be mitigating the vanishing gradient problem.

Randomly initializing the weights of the deep network could also be problematic and lead to the vanishing gradient problem. If we are using Sigmoid or Tanh as our activation functions, and many of the weights are initialized with values too small or too large, we will end up with derivatives close to zero. Using [He initialization](https://arxiv.org/abs/1704.08863) should prevent this from happening.

Finally, the vanishing gradient problem has nothing to do with the learning rate used to train the network, so the final choice is not a correct answer.

In summary, the first three choices are the correct answer to this question.

## References

- [On weight initialization in deep neural networks](https://arxiv.org/abs/1704.08863)
- [The Vanishing Gradient Problem. The Problem, Its Causes, Its Significance, and Its Solutions](https://towardsdatascience.com/the-vanishing-gradient-problem-69bf08b15484)
- [How to Fix the Vanishing Gradients Problem Using the ReLU](https://machinelearningmastery.com/how-to-fix-vanishing-gradients-using-the-rectified-linear-activation-function/)
- [Vanishing gradient problem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem)
