# Eden's schedule

Eden is building a deep learning model, but she is not having a lot of success getting it to converge.

One idea she wants to explore is to use a learning rate scheduler. Several of her colleagues recommended it, but she still isn't sure how this could help.

Eden decided that the first step for her is to understand how learning rate schedulers work.

**Which of the following is a correct definition of what a learning rate scheduler does?**

- [ ] The learning rate scheduler will help the optimization algorithm get past a flat region by continuing its previous movement.
- [ ] The learning rate scheduler will help the optimization algorithm accelerate in one direction based on past updates.
- [ ] The learning rate scheduler will save a copy of the network weights according to the value of the learning rate.
- [x] The learning rate scheduler will adjust the learning rate during training according to a pre-defined schedule.

## Answer

When training a neural network, setting the hyperparameters of the optimizer is essential for getting good results. One of the most critical parameters is the learning rate. Setting the learning rate too high or too low will cause problems during training.

A simple way to think about the [learning rate](https://en.wikipedia.org/wiki/Learning_rate) is as follows: if we set it too low, the training process will be slow; it will take a long time for the network to converge. Conversely, if we use a learning rate that's too high, the process will oscillate around the minimum without converging.

A popular technique to find a good balance is to use a learning rate scheduler. This predefined schedule adjusts the learning rate between epochs or iterations as the training progresses.

The most common scenario is to start with a high learning rate and decrease it over time. In the beginning, we take significant steps towards the minimum but move more carefully as we hone in on it.

The first two choices of this question refer to [momentum](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Momentum). A learning rate scheduler's goal is neither rolling by flat regions nor accelerating in one direction based on previous updates. The third choice is also incorrect since a learning rate scheduler has nothing to do with saving the learning rate.

## References

- ["Learning Rate Scheduling"](https://d2l.ai/chapter_optimization/lr-scheduler.html) is a great introduction to learning rate schedulers.
- ["How to Choose a Learning Rate Scheduler for Neural Networks"](https://neptune.ai/blog/how-to-choose-a-learning-rate-scheduler) is an article from [Neptune AI](https://neptune.ai/), focusing on some practical ideas on how to use schedulers.
