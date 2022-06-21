# The elbow method

After using a clustering algorithm on her dataset, Veronica fell in love with how easy it was to set everything up, run it, and get quick results back. After years of experience with supervised learning methods, K-Means was a breath of fresh air.

It took her some time to go through the documentation, and while reading online, she kept bumping into the "elbow method." It was clear that she needed to understand more about it.

**Which of the following statements is true about the elbow method?**

- [ ] In cluster analysis, the elbow method is used to determine the existing biases in a dataset.
- [ ] In cluster analysis, the elbow method is used to select the outliers in a dataset.
- [x] In cluster analysis, the elbow method is used to determine the optimal number of clusters.
- [ ] In cluster analysis, the elbow method is used to determine the features that better explain the patterns in a dataset.

## Answer

The story doesn't tell us, but I'm sure Veronica discovered something very early: No matter how many clusters she specified, the algorithm was happy to oblige. When she wanted 2 clusters, she got them. When she wanted 10, here they were.

The **elbow method** is a way to determine the optimal number of clusters.

Veronica is running K-means. She could run the algorithm on her dataset for a range of values of `k`, and for each value, calculate the sum of squared errors. Then, she could plot a line chart of these errors for each value of `k`. If the line chart [looks like an arm](https://en.wikipedia.org/wiki/Elbow_method_(clustering)#/media/File:DataClustering_ElbowCriterion.JPG), then the "elbow" on the arm is the best number of clusters (`k`) that she should use.

The elbow method is a way to choose the point where diminishing returns are no longer worth the cost. It's a very popular technique when using clustering algorithms.

Therefore, the third choice is the correct answer.

## Reading

- Check ["Using the elbow method to determine the optimal number of clusters for k-means clustering"](https://bl.ocks.org/rpgove/0060ff3b656618e9136b) for an explanation of how to use the elbow method.
- ["Elbow method (clustering)"](https://en.wikipedia.org/wiki/Elbow_method_(clustering)) is the Wikipedia page covering the elbow method.
- Check ["Knee of a curve"](https://en.wikipedia.org/wiki/Knee_of_a_curve) for a precise explanation of looking at the "elbow" of a curve.
