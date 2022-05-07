# Sometimes, small is better

Fynn is new to a team working on a neural network model. Unfortunately, they haven't been happy with the results so far.

Fynn thinks that he found the problem: they chose a batch size as large as it fits into the GPU memory. His colleagues believe this is the right approach, but Fynn believes a smaller batch size will be better.

**What would be good arguments to support Fynn's suspicion?**

- [ ] A smaller batch size is more computationally effective.
- [x] A smaller batch size reduces overfitting because it increases the noise in the training process.
- [ ] A smaller batch size reduces overfitting because it decreases the noise in the training process.
- [x] A smaller batch size can improve the generalization of the model.

## Answer

Choosing the right batch size is very specific to the problem at hand. We don't have much information about Fynn's use case here, but we can try and make an informed decision with the little we know.

Something important to notice here: "small" and "large" are relative ways to measure the size of a batch. A 32-sample batch is "small" if we compare it to 512, but it's large if you think of a single sample per batch. For this explanation, since Fynn's team was maximizing the amount of data that fit their hardware, assume that "large" refers to "a very large—almost ridiculous—amount of data."

Let's start by thinking about computational efficiency, where there's a tradeoff to consider. Modern GPU architectures are very good at optimizing the processing of large amounts of data, so packing more at once will be more efficient than trying to run multiple cycles. At the same time, computing the gradient over a massive amount of data is much more costly than computing the gradient of a very few samples.

So which one is it? Is it faster to fit as much data as possible in the GPU, or is it better to keep the batch as small as possible in this case? It's hard to tell without experimenting with the data for this specific problem, so this is not a clear argument for Fynn to justify using smaller batches.

If we use a small batch size, the optimizer will only see a small portion of the data during every cycle. This introduces noise in the training process because the gradient of the batch may take you in entirely different directions. However, on average, you will head towards a reasonable local minimum like you would using a larger batch size. Here is Jason Brownlee on **"How to Control the Stability of Training Neural Networks With the Batch Size"**:
> Smaller batch sizes are noisy, offering a regularizing effect and lower generalization error.

This noise may help the algorithm jump out of a sub-optimal local minimum and, hopefully, head towards a better local minimum or the global minimum. Fynn's model is not doing great, so lowering the generalization error is something that may help the team overcome their current challenges. Therefore, the second choice is correct, but the third one is not.

Finally, reducing the batch size often results in better model generalization. This is due to the regularization effect we mentioned before. Therefore, the last choice is correct as well.

By the way, if you are wondering which value to choose for the batch size in the beginning, follow the advice of Yoshua Bengio in **"Practical recommendations for gradient-based training of deep architectures"**:
> The mini-batch size is typically chosen between 1 and a few hundred, e.g., b = 32 is a good default value.

## References

- [Practical recommendations for gradient-based training of deep architectures](https://arxiv.org/abs/1206.5533)
- [How to Control the Stability of Training Neural Networks With the Batch Size](https://machinelearningmastery.com/how-to-control-the-speed-and-stability-of-training-neural-networks-with-gradient-descent-batch-size/)
