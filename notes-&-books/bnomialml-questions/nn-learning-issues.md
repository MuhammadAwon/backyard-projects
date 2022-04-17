# The mysterious case of the strange loss

Jena has finally finished building a neural network!

It took her some time to deal with the dataset, but she is finally ready to train the model.

Fifteen minutes later, Jena notices that her loss is not decreasing as expected. The loss stays high for the first few epochs, followed by a sudden reduction during the final epochs.

Jena was hoping for a steady decrease, so she got back to the drawing board to investigate what could be happening.

After a couple of hours, Jena has come up with a few potential reasons for the strange behavior.

**Which of the following could be causing the loss to behave this way?**

- [x] The regularization that Jena is using is too aggressive.
- [x] Jena is using a learning rate that's too low.
- [x] The neural network is getting stuck at local minima.
- [ ] Jena is using a learning rate that's too high.

## Answer

Many factors can cause problems during training. Let's discuss some of the more common ones.

Regularization is a helpful technique to avoid overfitting, but it may prevent the network from learning when it is too aggressive. This happens because regularization imposes a penalty on the network's weights, preventing them from becoming too large. If we aren't careful, the weights may stop changing, and the network will stop learning.

Another problem may be that the optimization is stuck in a local minimum. Strategies to overcome this problem include using a better initialization of the network's parameters or increasing the learning rate or momentum to overcome the local minimum.

A learning rate that is too low can have other adverse effects. The network weights will only be updated very slowly, so the loss will also decrease very slowly with time.

The only incorrect answer is assuming that Jena is using a learning rate that's too high. If this were the case, Jena would see rather significant changes in the loss. It is also common to see the loss oscillating after some time.

In summary, the first three choices are correct answers to this question.

## References

- [What should I do when my neural network doesn't learn?](https://stats.stackexchange.com/questions/352036/what-should-i-do-when-my-neural-network-doesnt-learn)
- [A Recipe for Training Neural Networks](http://karpathy.github.io/2019/04/25/recipe/)
