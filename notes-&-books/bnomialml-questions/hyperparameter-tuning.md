# The true meaning of hyperparameter tuning

Marlene is trying to build an audience.

Writing content seems easy, but taking a complex subject and boiling it down to its essence is not an obvious task.

Marlene wants to start from the basics and write as much as possible about the fundamentals of machine learning.

She picked her first topic: hyperparameter tuning.

**If you were trying to summarize the core idea of hyperparameter tuning, which one of the following sentences would you use?**

- [ ] Hyperparameter tuning is about choosing the set of optimal features from the data to train a model.
- [ ] Hyperparameter tuning is about choosing the set of optimal samples from the data to train a model.
- [x] Hyperparameter tuning is about choosing the optimal parameters for a learning algorithm to train a model.
- [ ] Hyperparameter tuning is about choosing the set of hypotheses that better fit the goal of the model.

## Answer

We use the term "hyperparameter" to refer to the parameters and settings that we can use to control the learning process. These are the "knobs" and "levers" that we can control from a learning algorithm.

In contrast, we use "parameters" to refer to variables internal to a model whose values we estimate during the learning process using data.

A good way of thinking about this:

- Parameters: We can't control them manually. We learn their values during training.
- Hyperparameters: We do control them manually. They act like configuration settings for our models.

Each model has different hyperparameters: You can control the depth of a decision tree or the step size during the optimization process of a neural network.

Understanding this should be enough to analyze the four choices for this question.

Hyperparameters have nothing to do with the data, so the first and second choices are incorrect answers. They aren't about features or samples.

The fourth choice is somewhat attractive. A good set of hyperparameters will indirectly lead to a better-fitted model, but "tuning hyperparameters" is not about "choosing a better hypothesis." Therefore, this choice is not correct.

The third choice is the one that best describes what hyperparameter tuning is about: choosing the best set of parameters to tune a learning algorithm.

## References

- [Overview of hyperparameter tuning](https://cloud.google.com/ai-platform/training/docs/hyperparameter-tuning-overview)
- [Hyperparameter optimization](https://en.wikipedia.org/wiki/Hyperparameter_optimization)
- [What is the Difference Between a Parameter and a Hyperparameter?](https://machinelearningmastery.com/difference-between-a-parameter-and-a-hyperparameter/)
