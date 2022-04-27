# Susan needs to make a decision

The deadline is approaching, and Susan still hasn't decided which version of her classification model to deploy to production.

She experimented with different hyperparameters, and now she has two models that perform pretty well.

Her problem is that none of these models is better than the other in every situation. One model has a higher recall but worse precision than the other. Susan can improve the precision by playing with different thresholds, but now the recall decreases.

**How can Susan decide which is the best overall model?**

- [ ] Susan should tune the thresholds until both have a recall of 95% and choose the one with higher precision.
- [ ] Susan should tune the thresholds until both have a precision of 95% and choose the one with a higher recall.
- [x] Susan should compute the area under the curve for both models and choose the one with the higher value.
- [ ] There's no objective way to decide which model is best. Susan should pick either one of them.

## Answer

Which model is better usually depends on the application. For some use cases, high recall is more important than precision, while in others, it is not.

However, contrary to the fourth choice, there is an objective way to determine which model is better overall.

The first two options suggest fixing one particular metric and choosing the model that performs the best on the other one. This is a valid approach, but it's not what Susan needs. Susan wants to determine which model is the best, but fixing either recall or precision won't return the best overall model since we would always be prioritizing one of the metrics.

For example, imagine that we tune both models to a recall above `90%` and then pick the one with the higher precision. There's no guarantee that the model we choose is the best possible model overall —the one that better balances recall and precision. Instead, we just ensured that the model we picked was the best model with a recall above `90%`.

To find the best overall model, Susan should compute the area under the ROC curve (Receiver Operating Characteristic) and choose the model with the higher value.

A ROC curve is a graph showing the True Positive Rate and the False Positive Rate at different classification thresholds. The area under this curve measures the performance of the model. A perfect model will have an area of `1.0`, while a model that only makes mistakes will have an area of `0.0`. Therefore, choosing the model with the higher area will give Susan the best overall model.

Therefore, the third choice is the correct answer to this question.

## References

- [ROC and AuC](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)
- [ROC metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
- [Area under the curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve)
