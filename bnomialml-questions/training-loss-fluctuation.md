# I'm frustrated with my training loss

I'm sure you've been here before.

I've been working on this neural network for a while. I'm using Mini-Batch Gradient Descent, and the results show the training loss oscillating up and down.

It is so frustrating!

I've been expecting it to go down consistently as my model learns, but I haven't had any luck so far.

Honestly, I don't have too much time left to deal with this, so I'll try one or two more things before I give up.

**Which of the following do you think I should try next?**

- [ ] This is clearly a problem with the data. I should go back to the dataset and ensure it's appropriately balanced.
- [ ] I should increase the learning rate to take larger steps in the direction of the gradient.
- [x] I should decrease the learning rate to avoid missing the local minima.
- [x] I should increase the batch size to increase the variability of samples on every batch.

## Answer

Let's start by focusing on the first option. The problem with the training loss is unlikely to be related to an imbalanced dataset. If that were the case, we would see a model struggling to learn anything, but we wouldn't see the loss oscillating back and forth.

The following two choices focus on the learning rate. Should we increase it or decrease it?

As the second option suggests, increasing the learning rate will allow us to take larger steps in the gradient's direction, but this means that we may miss the local minima!

If we miss the local minima, we have to get back. If the learning rate is too large, the same thing will happen: we'll miss the local minima and start oscillating back and forth. Therefore, the second choice is not correct either.

The last two choices are both sensible approaches to try.

If we reduce the learning rate, we can fix the oscillating loss if the problem is caused because the algorithm misses the local minima. This is a correct answer.

Finally, suppose the batch we are using is too small. In that case, we might see bad samples cause significant shifts in the training loss from one batch to another. Increasing the size of the batches and ensuring the data is distributed correctly could also help with the oscillating loss. This is also a correct answer.

## References

- [What could an oscillating training loss curve represent?](https://ai.stackexchange.com/questions/14079/what-could-an-oscillating-training-loss-curve-represent)
- [Why is my training loss fluctuating?](https://www.researchgate.net/post/Why_is_my_training_loss_fluctuating)
