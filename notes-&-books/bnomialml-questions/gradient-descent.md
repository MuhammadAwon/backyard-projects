# Emma's list

Nothing is perfect.

And no matter how much they said otherwise, Emma knew that gradient descent was no exception.

They have been discussing some of the most popular optimization algorithms for neural networks, and the team didn't want to listen despite Emma's comments regarding some of the downsides of gradient descent.

Emma decided to post a detailed list of problems on the company's Slack channel.

**Which of the following practical issues of gradient descent deserve to be on Emma's list?**

- [x] Gradient descent can take a long time to converge to a local minimum.
- [x] There's no guarantee that gradient descent will converge to the global minima.
- [x] Gradient descent is susceptible to the initialization of the network's weights.
- [ ] Gradient descent is not capable of optimizing continuous functions.

## Explanation

Gradient descent is one of the most popular optimization algorithms used in machine learning applications. But, despite its popularity, there are several practical issues that Emma wanted to mention.

The first issue is how gradient descent updates the model parameters after calculating the derivatives for all the observations. When working with large datasets, finding a local minimum may take a long time because the algorithm needs to compute many gradients before making a single update. [Stochastic Gradient Descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) (SGD), a variation of gradient descent, works differently and updates the model parameters for each observation speeding up the process. Since the team is focusing on gradient descent, the first choice made it to Emma's list.

The second choice is also on the list. Assuming the are multiple local minima in a problem, there is no guarantee that gradient descent will find the global minimum. Here is an excerpt from *"Gradient Descent*," a publication from the Computer Science Department of the University of Maryland:

> When a problem is nonconvex, it can have many local minima. And depending on where we initialize gradient descent, we might wind up in any of those local minima since they are all fixed points.

But it doesn't end there. As the previous quote mentions, gradient descent is also susceptible to the initialization of the network's weights. Assuming there are multiple local minima, the initialization of the network weights will play a fundamental role in whether the algorithm finds the global minimum: it may converge to a less optimal solution if we initialize the network too far from the global minimum. Therefore, the third choice is also a correct answer.

Finally, gradient descent can optimize a continuous function with no issues, so the fourth choice is not a correct answer.

In summary, Emma included the first three choices on her list.

## Recommendations

- [Gradient Descent](http://www.cs.umd.edu/~djacobs/CMSC426/GradientDescent.pdf) is a deep dive into gradient descent and its variants from the Computer Science Department of the University of Maryland.
- [Problems with Gradient Descent](https://www.encora.com/insights/problems-with-gradient-descent)
- [Gradient Descent For Machine Learning](https://machinelearningmastery.com/gradient-descent-for-machine-learning/)

