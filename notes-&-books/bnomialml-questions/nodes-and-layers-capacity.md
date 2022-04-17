# We need more capacity

As the business grew, Amelia saw their primary dataset balloon in size.

The neural network model they had running in production was starting to show severe issues. Amelia knew they had to make a change.

The issue was straightforward: the company has been collecting more features from a more varied customer base. Their current model was barely using a sliver of the available information, and it was clearly underfitting.

Amelia knew they had to increase the capacity of the model.

**Which of the following are steps that Amelia can take to increase the capacity of her neural network model?**

- [ ] Amelia should increase the learning rate to train the model.
- [x] Amelia should increase the number of hidden layers the neural network uses.
- [ ] Amelia should increase the regularization she is applying to the model.
- [ ] Amelia should increase the batch size to train the model.

## Answers!

From ["How to Control Neural Network Model Capacity With Nodes and Layers"](https://machinelearningmastery.com/how-to-control-neural-network-model-capacity-with-nodes-and-layers/):
> The capacity of a deep learning neural network model controls the scope of the types of mapping functions that it is able to learn. (...) The capacity of a neural network model is defined by configuring the number of nodes and the number of layers.

As we add more layers to a neural network, we increase its capacity. By adding more nodes to the layers, we also increase its capacity. Therefore, the second choice is the correct answer to this question.

The learning rate, regularization methods, and batch size do not influence the network's capacity.

## References
* [How to Control Neural Network Model Capacity With Nodes and Layers](https://machinelearningmastery.com/how-to-control-neural-network-model-capacity-with-nodes-and-layers/)
* [The capacity of feedforward neural networks](https://www.math.uci.edu/~rvershyn/papers/bv-capacity-neural-networks.pdf)