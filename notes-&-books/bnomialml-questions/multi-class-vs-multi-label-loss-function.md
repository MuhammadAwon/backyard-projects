# Arya's confusion

Arya is always confused about this.

We have multi-class classification problems when every sample in the dataset belongs to one class. We have multi-label classification problems when every instance belongs to one or more categories.

These types of problems look similar, but they are very different.

Arya never remembers the correct loss function to train a neural network to solve these problems.

**Which two of the following statements are correct?**

- [x] Binary cross-entropy is the loss function used for multi-label classification problems.
- [ ] Binary cross-entropy is the loss function used for multi-class classification problems.
- [ ] Categorical cross-entropy is the loss function used for multi-label classification problems.
- [x] Categorical cross-entropy is the loss function used for multi-class classification problems.

## Answer

The goal of the output layer of a [multi-class classification](https://en.wikipedia.org/wiki/Multiclass_classification) model is to return the class that better represents the network's input. Softmax is ideal because it uses the output score to produce a probability for each category.

The categorical cross-entropy loss function quantifies the difference between two probability distributions. When working on multi-class classification tasks, the categorical cross-entropy is the perfect loss function to pair with a softmax output layer.

In the case of [multi-label classification](https://en.wikipedia.org/wiki/Multi-label_classification) models, our output layer should return values independent from each other. Sigmoid is perfect because it converts the output scores to a value between 0 and 1.

Multi-label classification problems borrow the same principles from binary classification problems. The difference is that we end up with multiple sigmoid outputs instead of one. It's helpful to think of a model that outputs ten possible classes as a combination of ten different binary classifiers. Remember the loss function we use to train binary classification models? Binary cross-entropy.

In summary, multi-class classification models should use a softmax output with the categorical cross-entropy loss function. Multi-label classification models should use a sigmoid output and the binary cross-entropy loss function.

## Reading

- Check ["Binary crossentropy"](https://peltarion.com/knowledge-center/documentation/modeling-view/build-an-ai-model/loss-functions/binary-crossentropy) for an explanation of how Binary Cross-Entropy works.
- Check ["Categorical crossentropy"](https://peltarion.com/knowledge-center/documentation/modeling-view/build-an-ai-model/loss-functions/categorical-crossentropy) for an explanation of how Categorical Cross-Entropy works.
