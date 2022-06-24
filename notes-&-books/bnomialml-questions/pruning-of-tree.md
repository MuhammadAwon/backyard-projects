# Pruning the tree

Ana has been scratching her head for a while.

She is using a Decision Tree on a dataset, and although her training performance is excellent, the test performance is terrible.

After discussing with her professor, the recommendation was to prune the tree, but Ana didn't understand why this would solve the problem.

**Which statements explain why pruning the tree will solve Ana's problem? Select all that apply.**

- [x] By pruning the Decision Tree, Ana will increase the model's bias.
- [ ] By pruning the Decision Tree, Ana will increase the model's variance.
- [ ] By pruning the Decision Tree, Ana will decrease the model's bias.
- [x] By pruning the Decision Tree, Ana will decrease the model's variance.

## Answer

A Decision Tree is an algorithm with low bias and high variance. This means that a Decision Tree makes almost no assumptions about the target function.

Because of its high variance, Decision Trees tend to overfit easily to the training dataset. Ana saw this as soon as she tried the model on her test data.

To avoid overfitting, Ana should prune the tree. We force the tree to generalize better and make assumptions by reducing the number of nodes. In other words, by pruning the tree, we increase its bias and decrease its variance.

Therefore, the first and fourth choices are the correct answer.

## Reading

- ["Gentle Introduction to the Bias-Variance Trade-Off in Machine Learning"](https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/) is an excellent introduction to the bias and variance tradeoff.
- The Wikipedia page on bias and variance is also a good resource: ["Bias–variance tradeoff".](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)
- In case you like the simplicity of Twitter threads, here is one for you about this topic: ["Bias, variance, and their relationship with machine learning algorithms".](https://twitter.com/svpino/status/1390969728504565761)
