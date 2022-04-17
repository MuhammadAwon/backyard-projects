# Looking behind François's Tweet

Recently, François Chollet mentioned that you should never try to use a learning-rate schedule from an old dataset to train a new one.

Imagine a scenario where you create a deep learning classification model to train on images from a security camera. During the exploration phase, you set up a specific training schedule that works well for your problem and gives you good performance.

When training a new version of the model — even when using the same architecture — with images from a different security camera, François' advice is to avoid using the same training schedule.

**Which of the following could be François' thinking behind his advice?**

- [ ] The learning-rate schedule depends on the number of samples in the dataset, so the exact schedule won't work with a different size dataset.

- [ ] The learning-rate schedule should change whenever we have a dataset from a different target distribution. This won't be the case if the target distribution is the same.

- [x] A new dataset changes the tradeoff between optimization and regularization. The learning-rate schedule is dataset-specific.

- [ ] Learning-rate schedules are specific to the optimization mechanisms used by the model. A new dataset usually requires that we change the optimization process, which will invalidate the learning-rate schedule as well.

## The Answer

Here is François's Tweet:
> PSA: never attempt to use a training schedule from an old dataset on a new dataset. Even if the model, the number of samples, and the target distribution are the same, the intrinsic difficulty of the problem may have changed (tradeoff between optimization and regularization). Learning rate schedules and regularization are fundamentally dataset-specific, far more than model architecture.

Notice that he mentions that even when the dataset size and the target distribution are the same, the learning-rate schedule might not be helpful anymore. Therefore, neither the first nor second choices are correct.

The fourth choice argues that the issue is because of a likely change in the optimization process, which is not the case. Even when we don't change anything about the model architecture or the method we use to train it, a new dataset may change the intrinsic difficulty of the problem.

By using a different dataset, the problem's difficulty may change. We may need more regularization to avoid overfitting. We may need less regularization to make sure the model learns the specifics of the problem. A different dataset means a different set of tradeoffs.

## References

- [François's Tweet](https://twitter.com/fchollet/status/1508477486882979843)
- [Deep Learning with Python, Second Edition](https://amzn.to/3K3VZoy)