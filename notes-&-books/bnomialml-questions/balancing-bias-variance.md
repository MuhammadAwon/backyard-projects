# Balancing bias and variance

The very first chapter of her machine learning book was about bias, variance, and their tradeoff.

Callie knew that she had no alternative: she had to spend the time trying to understand these concepts before moving on.

But at the end of the day, it wasn't easy to remember the nuances of each concept, so Callie decided to get help.

**Which of the following descriptions of bias and variance are correct?**

- [x] Bias refers to the assumptions a model makes to simplify the process of finding answers. The more assumptions it makes, the more biased the model is.
- [ ] Variance refers to the assumptions a model makes to simplify finding answers. The more assumptions it makes, the more variance in the model.
- [ ] Bias refers to how much the answers given by the model will change if we use different training data. The model has low bias if the answers stay the same regardless of the data.
- [x] Variance refers to how much the answers given by the model will change if we use different training data. The model has low variance if the answers stay the same regardless of the data.

## Explanation

Every machine learning algorithm deals with three types of errors:

- Bias error
- Variance error
- Irreducible error

To answer this question, let's forget about the irreducible error and focus on the other two.

Here is what **Jason Brownlee** has to say about bias:
> Bias are the simplifying assumptions made by a model to make the target function easier to learn.

Think about a simple linear model. It assumes that the target function is linear, so the model will try to fit a line through the data regardless of its appearance. This assumption helps the model simplify the process of finding the answer, and the more assumption it makes, the more biased the model is. Often, linear models are high-bias, and nonlinear models are low-bias.

Here is a [funny depiction of biases](https://xkcd.com/2618/): the speaker believes everyone must understand selection bias. Whenever we put people in buckets to characterize or predict how they act, we use our biases to simplify our understanding of the world.

![](https://user-images.githubusercontent.com/1126730/168139417-8e5d8ce5-929e-4f8f-96a1-80232d61c73e.png)

Regarding variance, **Jason** continues:
> Variance is the amount that the estimate of the target function will change if different training data is used.

Variance refers to how much the answers given by the model will change if we use different training data. The model has low variance if the answers stay the same regardless of the data.

Think about a fickle person that constantly changes their mind with the news. Every new article makes the person believe something completely different. I don't want to overextend the analogy, but this is an example of high variance. Often, linear models are low-variance, and nonlinear models are high-variance.

If we consider all of this, the first and fourth choices are the correct answer to this question.

## Recommendations

- Here is Jason Brownlee's article I mentioned before: ["Gentle Introduction to the Bias-Variance Trade-Off in Machine Learning"](https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/).
- The Wikipedia page on bias and variance is also a good resource: ["Bias–variance tradeoff"](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff).
- In case you like the simplicity of Twitter threads, here is one for you about this topic: ["Bias, variance, and their relationship with machine learning algorithms"](https://twitter.com/svpino/status/1390969728504565761).
