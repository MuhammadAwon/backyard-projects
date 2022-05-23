# Scheduled learning

A company—a bad one, because there are plenty of those out there—has been experiencing some turnaround, and they wanted to ensure the new team members were up to speed with the neural network model they were using in production.

The team has been looking at the code and writing notes every time they find something new.

They stumbled upon the training scripts and noticed the last team used a learning rate scheduler.

**Which of the following statements could explain why the last team used this scheduler? Select all that apply.**

- [ ] The last team used the learning rate scheduler to increase the learning rate as training progressed.
- [x] The last team used the learning rate scheduler to decrease the learning rate as training progressed.
- [x] The last team used the learning rate scheduler to give the network a better chance to converge.
- [ ] The last team used the learning rate scheduler to save the learning rate at specific intervals during the training process.

## Answer

When training a neural network, setting the hyperparameters of the optimizer is essential for getting good results. One of the most critical parameters is the [learning rate](https://en.wikipedia.org/wiki/Learning_rate). Setting the learning rate too high or too low will cause problems during training.

A simple way to think about the learning rate is as follows: if we set it too low, the training process will be very slow; it will take a long time for the network to converge. Conversely, if we use a learning rate that's too high, the process will oscillate around the minimum without converging. Here is a chart from ["Deep Learning Wizard"](https://www.deeplearningwizard.com/deep_learning/boosting_models_pytorch/lr_scheduling/) illustrating the effect of different learning rates:

<img src="https://user-images.githubusercontent.com/1126730/167927199-f6a2add7-91be-4bc6-8459-bf00ff0ea4b6.png"/>

A popular technique to find a good balance is to use a learning rate scheduler. This predefined schedule adjusts the learning rate between epochs or iterations as the training progresses.

The most common scenario is to start with a high learning rate and decrease it over time. In the beginning, we take significant steps towards the minimum but move more carefully as we hone in on it.

Looking at the available choices, we can see the first choice is incorrect, but the second and third choices are correct. The team was likely trying to decrease the learning rate as training progressed. Although there are experiments showing the use of **cyclical learning rates**, the most common practice when using a scheduler is to start with a high learning rate and reduce it over time.

Finally, the fourth choice is incorrect as well. A learning rate scheduler has nothing to do with saving the learning rate.

In summary, the second and third choices are the correct answers to this question.

## Recommendations

- ["Learning Rate Scheduling"](https://d2l.ai/chapter_optimization/lr-scheduler.html) is a great introduction to learning rate schedulers.
- ["How to Choose a Learning Rate Scheduler for Neural Networks?"](https://neptune.ai/blog/how-to-choose-a-learning-rate-scheduler) is an article from Neptune AI, focusing on some practical ideas on how to use schedulers.
- ["Cyclical Learning Rates for Training Neural Networks"](https://arxiv.org/abs/1506.01186) is the paper discussing a technique to let the learning rate cyclically vary between reasonable boundary values.
