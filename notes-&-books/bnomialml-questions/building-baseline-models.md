# Two similar models

One of the most critical steps in your machine learning process is selecting a good baseline.

Before you start looking into more complex problems, a simple baseline gives you a solid foundation to understand where you are and what improvements you can make.

Margot and Jan wanted to use a different algorithm to build their baseline. Jan wanted to go with a simple neural network, but Margot argued for using a linear regression model.

They didn't want to pick, so they decided to try each baseline and choose the best one. But before starting, Margot and Jan agreed to research the similarities between both models so they could reuse as much as possible when building them.

They wrote down a list.

**Which of the following are true about Jan's neural network and Margot's linear regression model?**

- [x] Both models require every input feature to be a numeric value. Margot and Jan will need to transform every non-numeric feature to feed both baselines.
- [ ] Both models require every numerical input to be between 0 and 1. Margot and Jan will need to standardize every numeric feature and squeeze them into this range.
- [ ] Both models output a vector of probabilities. Margot and Jan can build a common logic to interpret the results of their respective baselines.
- [ ] Both models output the result of a linear sum of the weighted input values. Margot and Jan should be able to explain the results from their respective baselines in a similar fashion.

## Answer

I'd go with Margot on this one. A linear regression model sounds simpler to build a baseline than a neural network. The former is easy to set up and tune, while the latter will require much more work.

Of course, this is just a gut feeling. There's nothing on this problem that suggests one way or the other.

But that's not the question. We want to understand which of the four statements is something that both models have in common.

Starting with the first choice, both neural networks and linear regression models require the input features to be numeric. Neither works with categorical features. Decision Trees, for example, don't have this limitation, but these two models do. Therefore, Margot and Jan will need to transform non-numeric features before using them.

The second choice is interesting because it's usually the case that both models work better if their input features are appropriately scaled or standardized. Training a model with a feature ranging from 0 to 10,000 and another feature ranging from 0 to 1 is never a good recipe. However, neither one of these models requires features within 0 and 1, so this is not a correct statement.

The third choice is not correct either. The output of a linear regression model is a single numerical value, not a vector of probabilities. There's also no requirement for a neural network to have such an output.

Finally, while both linear regression and neural networks use a linear sum of weighted inputs, neural networks introduce non-linearities in the form of activation functions. This is a crucial difference. It makes neural networks much more powerful than linear regression, but at the same time, it makes it much harder to explain the results.

In summary, the correct answer to this question is the first choice.

## References

- Check ["Linear Regression v.s. Neural Networks"](https://towardsdatascience.com/linear-regression-v-s-neural-networks-cd03b29386d4) for a comparison between these two techniques.
- ["3 Reasons Why You Should Use Linear Regression Models Instead of Neural Networks"](https://www.kdnuggets.com/2021/08/3-reasons-linear-regression-instead-neural-networks.html) is another great article talking about their differences.
- ["Linear Regression for Machine Learning"](https://machinelearningmastery.com/linear-regression-for-machine-learning/) is a great introduction to linear regression.
- ["Intro to Neural Networks"](https://developers.google.com/machine-learning/crash-course/introduction-to-neural-networks/video-lecture) is a good summary of neural networks.
