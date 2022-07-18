# Increasing dropout

Quinn's approach to learning something new is to run as many experiments as she needs to grasp how things work.

Today, it was the turn of Dropout.

Quinn wants to know how it works, and one of her experiments is to increasingly modify the Dropout rate in a neural network and see how it affects the model's accuracy on the test data.

**Which of the following do you think is the result that Quinn will observe after running this experiment?**

- [ ] As the Dropout rate increases, the accuracy will go down until it hits a low value.
- [ ] As the Dropout rate increases, the accuracy will go down, and at some point, it will begin to increase.
- [ ] As the Dropout rate increases, the accuracy will go up until it hits its maximum potential.
- [x] As the Dropout rate increases, the accuracy will go up, and at some point, it will begin to decrease.

## Answer

Dropout is a regularization method that works well and is vital for reducing overfitting.

Sometimes, the nodes in a neural network create strong dependencies on other nodes, which may lead to overfitting. An example is when a few nodes on a layer do most of the work, and the network ignores all the other nodes. Despite having many nodes on the layer, you only have a small percentage of those nodes contributing to predictions. We call this phenomenon "[co-adaptation](https://machinelearning.wtf/terms/co-adaptation/)," and we can tackle it using Dropout.

During training, Dropout randomly removes a percentage of the nodes, forcing the network to learn in a balanced way. Now every node is on its own and can't rely on other nodes to do their work. They have to work harder by themselves.

As Quinn increases the Dropout rate, she will reduce overfitting and see the model's accuracy improve. At some point, however, the rate will be so high that the model will start underfitting, and the accuracy will come down. This drop happens because removing too many of the neurons during training will effectively reduce the model's capacity too much. In other words, while some regularization is good, too much of it will prevent the model from learning.

Therefore, the fourth choice is the correct answer to this question.

## References

- For more information about co-adaptation and how to use Dropout, check ["Improving neural networks by preventing co-adaptation of feature detectors".](https://arxiv.org/pdf/1207.0580.pdf)
- ["A Gentle Introduction to Dropout for Regularizing Deep Neural Networks"](https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/) is an excellent introduction to Dropout.
