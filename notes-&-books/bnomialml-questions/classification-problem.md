# The bankruptcy story

Suzanne wants to build an algorithm to predict whether a company is about to declare bankruptcy over the next few months.

She has access to a labeled dataset with detailed financial information from thousands of companies, including those that have declared bankruptcy over the last 100 years.

Suzanne has some ideas but would love to hear what you think.

**Understanding that there are many ways to approach a problem, what would be your first recommendation to Suzanne?**

- [ ] The best way to approach this problem is with Supervised Learning by using a regression algorithm.
- [x] The best way to approach this problem is with Supervised Learning by using a classification algorithm.
- [ ] The best way to approach this problem is with Unsupervised Learning by using a clustering algorithm.
- [ ] The best way to approach this problem is with Reinforcement Learning.

## Answer

Suzanne is trying to answer a question with only two possible answers: Is this company going to declare bankruptcy or not?

There could be many ways to approach this problem, but we can go with what we know in this case.

Suzanne has access to labeled data, so she could set some of her data aside for testing purposes and build a binary classification model to predict a binary target value. This target could be whether or not the company declared bankruptcy.

This is likely the more straightforward way to approach Suzanne's problem: A Supervised Learning binary classification model.

Could we reframe this as a regression problem? Maybe. It would depend on the data we have for each company, but nothing in the description points to that being a good strategy.

Clustering could also be helpful, but since Suzanne has labeled data, clustering shouldn't be the first recommendation. The same happens with reinforcement learning, which seems to be a stretch based on what we know about this problem.

This leaves us with the second choice as the correct answer.

## References

- [Supervised and Unsupervised Machine Learning Algorithms](https://machinelearningmastery.com/supervised-and-unsupervised-machine-learning-algorithms/)
- [What is supervised learning?](https://www.ibm.com/cloud/learn/supervised-learning)
