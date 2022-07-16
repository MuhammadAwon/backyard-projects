# Evaluating object detection

Rose started a new job, and her first task was to develop an object detection model that detects cars in drone footage.

Rose wanted to build a generic model that she could use for different applications.

It would help if she had some solid evaluation of the model's performance to compare different versions and choose the best one.

**Which evaluation metrics should Rouse use to evaluate her model?**

- [] Recall
- [] ROC Curve
- [] Precision-Recall Curve
- [] F1 score

## Answer

The recall is a helpful metric for object detection, but it won't tell Rose the whole picture without looking at the precision. Rose could build a useless model with high recall but abysmal precision. Therefore, she can't use recall as the definitive metric.

There's a problem with [ROC Curves](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) for object detection problems: there's no concept of True Negatives, and the ROC curve needs it to display the False Positive Rate on one of the axes. On object detection, the number of bounding boxes that won't contain a relevant object is too large, and that's why we avoid any metrics that depend on True Negatives.

Instead, Rose can compute a [Precision-Recall Curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html). This curve is similar to the ROC curve, but instead of using the False Positive Rate, it uses the model's precision that doesn't depend on the True Negatives.

Finally, computing the [F1-score](https://en.wikipedia.org/wiki/F-score) is also an option because it considers both the precision and recall of the model.

## References

- Check ["Classification: ROC Curve and AUC"](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) for an explanation of how to create and interpret a ROC curve.
- For more information about Precision-Recall curves, check [Scikit-Learn's documentation.](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html)
