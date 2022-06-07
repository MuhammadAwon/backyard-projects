# Making email fun

Let's be honest: dealing with email is not fun.

Waking up to an inbox full of unsolicited messages is the worst way to kick off your day. Email applications do their best, but a lot of spam still gets through the cracks.

How about building your own personalized spam detection model?

One morning, Sue decided to do it, and after a few iterations, she ended with a working model.

Time to find out how good it is!

**Which method should Sue use to evaluate her spam detection model?**

- [ ] Sue should use the model's accuracy as defined by the percentage of legitimate messages that go through with respect to the total number of received emails.
- [ ] Sue should use the model's recall as defined by the percentage of detected spam messages with respect to the total of spam messages received.
- [ ] Sue should use the Fβ-Score of the model with a high value of β.
- [x] Sue should use the Fβ-Score of the model with a low value of β.

## Answer

Spam detection is an imbalanced problem: you will always have more legitimate emails than spam emails.

Whenever you need to work with an imbalanced dataset, accuracy will not be a good metric to decide how good your model is. You can achieve very high accuracy even with a model that does nothing useful. For example, if only 1% of the emails you receive are spam, by simply assuming none of it is spam, your model will be 99% accurate. Therefore, the first choice is not a good approach for Sue.

The recall is a helpful metric to understand how much spam you can detect, but by itself could also be deceiving. For example, Sue's model could flag every single email message as spam, which will give her a 100% recall. This, of course, it's not helpful, so the second choice is also not correct.

Using the **Fβ-Score**, however, is a good choice.

The Fβ score lets us combine precision and recall into a single metric. When using β = 1, we place equal weight on precision and recall. For values of β > 1, recall is weighted higher than precision; for values of β < 1, precision is weighted higher than recall.

You are probably familiar with F1-Score. F1-Score is just Fβ-Score with β = 1.

Sue doesn't want to flag valid legitimate messages as spam. Doing this runs the risk of people missing important emails. Therefore, a good strategy is to prioritize a system with high precision, so using a lower value of β is the way to go. Therefore, the correct answer is the fourth choice.

Notice that by prioritizing the precision of her model, Sue will let some spam messages through. Although this is not ideal, it's a better outcome than getting the spam filter to catch legitimate emails.

## References

- ["What is the F-Score?](https://deepai.org/machine-learning-glossary-and-terms/f-score) is a short introduction to this metric.
- For a more in-depth analysis of the Fβ-Score, check ["A Gentle Introduction to the Fbeta-Measure for Machine Learning"](https://machinelearningmastery.com/fbeta-measure-for-machine-learning)
- Check ["Failure of Classification Accuracy for Imbalanced Class Distributions"](https://machinelearningmastery.com/failure-of-accuracy-for-imbalanced-class-distributions/) to understand why accuracy fails when working with imbalanced datasets.
