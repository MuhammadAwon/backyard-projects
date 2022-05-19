# Occam's Razor showoff

Tiara's manager was a showoff. No matter the situation, he always found a way to show everyone how smart he was.

Tiara noticed that he's been getting into machine learning lately, and as cringe as it sounds, he has been using "Occam's Razor" on every occasion, even incorrectly.

Tiara started a secret list collecting every scenario when her manager used Occam's Razor to explain a situation. At the end of the week, she sent it to many of her friends to have a good laugh.

**Which of the following situations from Tiara's list are you comfortable justifying with Occam's Razor?**

- [x] We should prefer simpler models with fewer coefficients over complex models like ensembles.
- [x] Feature selection and dimensionality reduction help simplify models to get better results.
- [ ] Keeping the training process as fast as possible avoids overtraining and prevents overcomplicated results.
- [ ] Starting the training of the model using sensible values for the hyperparameters.

## Answer

*Occam's Razor* is a principle that says that if you have two competing ideas to explain the same phenomenon, you should prefer the simpler one.

There are a couple of situations in this list where using Occam's Razor is a stretch. The third choice is probably the simplest one to tackle first: it talks about "the speed of the training process" and relates it to overtraining and overcomplicating results. Not only does this has nothing to do with Occam's Razor, but a quick training process doesn't necessarily reduce complexity.

The fourth choice is also not correct. Starting training using sensible values for the hyperparameters is essential, but we can't explain this using Occam's Razor.

Occam's Razor fits the first choice like a glove. Given two learning algorithms with similar tradeoffs, we should use the least complex and most straightforward to interpret. At least this time, Tiara's boss was correct.

Finally, the second choice is not an obvious fit, but we could argue it's also a correct answer. Feature selection and dimensionality reduction simplify the data we use to train our models. We use these steps to remove redundant or irrelevant information, therefore getting a simpler dataset that should perform better than a more complex one.

In summary, Tiara's manager was correct on the first two but was incorrect on the last two.

## References

- [Ensemble Learning Algorithm Complexity and Occam’s Razor](https://machinelearningmastery.com/ensemble-learning-and-occams-razor/)
- [How does Occam's razor apply to machine learning?](https://www.techopedia.com/how-does-occams-razor-apply-to-machine-learning/7/33087)
- The [*Occam's razor*](https://en.wikipedia.org/wiki/Occam%27s_razor) definition in Wikipedia.
