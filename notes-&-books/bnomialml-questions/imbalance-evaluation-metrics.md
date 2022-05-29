# Choosing the wrong metric

Let's assume you are working with a severely imbalanced dataset.

We've all been there. It's a pretty typical scenario.

Now let's imagine you want to split the data into two categories using a classification learning algorithm.

It's hard to pick the best evaluation metric for this problem if we don't know what we want to accomplish. But at least we can rule out the ones that we shouldn't use.

**Which of the following metrics should you avoid using when evaluating your model's performance?**

- [ ] Recall
- [ ] Precision
- [ ] F1-Score
- [x] Accuracy

## Explanation

Let's illustrate this with a hypothetical example.

Let's imagine that your team wants to build a machine learning model to predict whether a specific car will get in an accident.

You are pretty funny, so you decide to play a prank on everyone else by committing this as a solution to the problem:

```Python
def is_the_car_going_to_crash_today():
    return False
```

Your team evaluates the model against a test set, and your dummy code is 99% accurate!

The National Safety Council reports that the odds of being in a car crash in the United States are less than 1%. This means that even the dumb function above will be very accurate!

The problem here is probably obvious by now: Accuracy is not a good metric when you face a very imbalanced problem. You can achieve very high accuracy even with a model that does nothing useful.

Some examples of imbalanced problems:

- Detecting fraudulent transactions
- Classifying spam messages
- Determining if a patient has cancer

The other three metrics will give you much more information than accuracy, depending on the problem and how you want to approach it.

In summary, the fourth choice is the correct answer to this question.

## Reading

- [Random Oversampling and Undersampling for Imbalanced Classification](https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/)
- Check ["Failure of Classification Accuracy for Imbalanced Class Distributions"](https://machinelearningmastery.com/failure-of-accuracy-for-imbalanced-class-distributions/) to understand why accuracy fails when working with imbalanced datasets.
- If you are into Twitter, [here is a much more detailed story](https://twitter.com/svpino/status/1357302018428256258) about predicting crashes with 99% accuracy.
