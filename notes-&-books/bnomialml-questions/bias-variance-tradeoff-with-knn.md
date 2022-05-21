# Zoe's looking into KNN

It was the first time Zoe dealt with k-Nearest Neighbors (KNN). She inherited the code, and now she was responsible for making it work.

Before touching the code, she decided to do some research. Her first stop was on one of the fundamental topics in machine learning: bias, variance, and their relationship with the algorithm.

She knows there's always a tradeoff between these two.

**Which of the following statements are correct concerning the bias and variance tradeoff of KNN?**

- [x] Zoe can increase the bias of KNN by using a larger value of `k`.
- [ ] Zoe can increase the variance of KNN by using a larger value of `k`.
- [x] Zoe can decrease the bias of KNN by using a smaller value of `k`.
- [ ] Zoe can decrease the variance of KNN by using a smaller value of `k`.

## Explanation

[KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) is an algorithm with low bias and high variance.

Let's imagine Zoe decides to use a small value of `k`, for example, `k=1`. In this case, the algorithm will likely predict the training dataset perfectly. The smaller the value of `k`, the less bias and larger variance KNN will show. This, of course, is not a great outcome because the model will overfit and have difficulty predicting unseen data.

Now let's assume Zoe decides to use a very large value of `k`; for example, set `k` to the number of samples on her training dataset. This will increase the algorithm's bias and reduce its variance, resulting in an underfit model that can't adequately capture the variance in the training dataset. Here is a quote from *"Why Does Increasing k Decrease Variance in kNN?"*:
> If we take the limit as k approaches the size of the dataset, we will get a model that just predicts the class that appears more frequently in the dataset [...]. This is the model with the highest bias, but the variance is 0 [...]. High bias because it has failed to capture any local information about the model, but 0 variance because it predicts the exact same thing for any new data point.

As Zoe suspects, neither case will lead to a proper solution. She needs to find the appropriate tradeoff between the bias and variance of the algorithm.

In summary, the smaller the value of `k` is, the lower the bias and higher the variance. The larger the value of `k` is, the higher the bias and lower the variance. This means that the first and third choices are correct: we can control the algorithm's bias as explained in these two choices.

## Recommendations

- ["Why Does Increasing k Decrease Variance in kNN?"](https://towardsdatascience.com/why-does-increasing-k-decrease-variance-in-knn-9ed6de2f5061) is a really good article diving into the relationship of `k` and the variance of KNN.
- For a more general introduction to the bias-variance trade-off, check ["Gentle Introduction to the Bias-Variance Trade-Off in Machine Learning"](https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/).
- In case you prefer Twitter threads with a summary of how this works, check out ["Bias, variance, and their relationship with machine learning algorithms"](https://twitter.com/svpino/status/1506964069646884864).
