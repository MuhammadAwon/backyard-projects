# A way to win Kaggle competitions

Victoria joined Kaggle, and halfway through her first competition, she realized her single model wouldn't perform very well on the leaderboard.

She learned that most people were using multiple models working together. Looking into that extra boost from ensembles was the only way she would be able to increase her score.

Victoria spent a couple of days reading about stacking and blending, two of the most popular techniques for building ensemble models. Although she was clear about the high-level idea, she wasn't sure about some of the differences between both techniques.

**Which of the following are valid differences between stacking and blending?**

- [ ] The meta-model created using stacking learns how to combine the predictions from multiple models. In contrast, the meta-model created using blending uses the predictions of the best contributing model.
- [x] Stacking doesn't need models of comparable predictive power. In contrast, blending works like a weighted average and requires models to contribute positively to the ensemble.
- [x] The meta-model created using stacking is trained on out-of-fold predictions made during cross-validation. In contrast, a meta-model created using blending is trained on predictions made on a holdout set.
- [ ] Stacking works well for both classification and regression problems. In contrast, Blending only works for regression problems.

## Answer

Victoria is right. Stacking and blending are powerful ensemble techniques and a must if you want to score high in Kaggle competitions.

Although both techniques have the same ultimate goal, there are essential differences in how they work. Let's start unraveling each of the available choices for this question to determine which ones are correct.

Stacking and blending use the concept of a "meta-model," a model that you train to average the results of other models. At a high level, both ensemble techniques use multiple models to generate predictions, and a meta-model to average those predictions and provide a final result.

The first choice argues that blending uses the predictions of the best contributing model, which is not true. Just like stacking, blending's meta-model uses the predictions of multiple models. Therefore, this is not a valid difference between both techniques.

An advantage of stacking is that it can benefit even from models that don't perform very well. In contrast, blending does require that models have a similar, good predictive power. Here is an excerpt from *"The Kaggle Book"*:

> (...) one interesting aspect of stacking is that you don't need models of comparable predictive power, as in averaging and often blending. In fact, even worse-performing models may be effective as part of a stacking ensemble.

So even when using an individual model that performs poorly compared to all of the other models used by the stacking ensemble, the meta-model can use its out-of-fold predictions to improve its performance. Therefore, the second choice is a valid difference between both techniques.

Another valid difference between stacking and blending is the data they use to train the meta-model. The stacking meta-model is trained in the entire training set, using the *out-of-fold* prediction strategy. The blending meta-model is trained in a holdout set that we randomly extract from the training dataset. Therefore, the third choice is also a valid difference between these techniques.

Finally, stacking and blending work well for regression and classification problems, so the final choice is incorrect.

In summary, the second and third choices are the correct answers to this question.

## References

- [Stacking and Blending — An Intuitive Explanation](https://medium.com/@stevenyu530_73989/stacking-and-blending-intuitive-explanation-of-advanced-ensemble-methods-46b295da413c)
- [Stacking Ensemble Machine Learning With Python](https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/)
- [Blending Ensemble Machine Learning With Python](https://machinelearningmastery.com/blending-ensemble-machine-learning-with-python/)
- [How to Use Out-of-Fold Predictions in Machine Learning](https://machinelearningmastery.com/out-of-fold-predictions-in-machine-learning/)
- [The Kaggle Book](https://amzn.to/3kbanRb)
