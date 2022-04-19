# Thinking about softmax

Remember the last time you built a machine learning multi-class classification model?

You probably used a softmax activation on the output layer of your network. It's a widespread practice, so there's a good chance you've done it.

It's usually fun to think about why we do things the way we do them, so let's get into it.

**Which of the following statements is true about the softmax activation function when used in the output layer of a neural network?**

- [ ] The softmax function turns the network's input into a vector of probabilities that sum to 1.
- [x] The softmax function is a probabilistic or "smooth" version of the function that returns the index of the vector's largest value.
- [ ] The softmax function turns a vector of real values into a sorted vector of probabilities that sum to 1.
- [ ] The softmax function is a probabilistic or "smooth" version of the function that returns the vector's maximum value.

## Answer

I'm not good with formal definitions, but here is a simplified explanation of what the softmax function does when used in the output layer of the network:
> The softmax function turns a vector of real values into another vector of probabilities that sum to 1. These probabilities are proportional to the relative scale of each value in the vector.

When used as the activation function of the output layer of a neural network, softmax converts the scores coming from the previous layer to a normalized probability distribution. This is a very convenient way to interpret the results of a multi-class classification model.

Let's look at the first choice for this question. It's a close one, but it's incorrect: Softmax doesn't convert the network's input into a vector of probabilities; it converts the vector from the previous layer.

The third choice is also close, but it talks about a "sorted vector of probabilities." Softmax doesn't sort the output vector, so this option is incorrect.

The remaining two options seem to be similar, but they aren't if you read them carefully.

The second choice talks about a function that returns the index of the largest value in the vector. We call this function `argmax`.

If we run a vector through the `argmax` function we will get the index of the largest value in the vector. From a probabilistic perspective, the largest value will be assigned `1` while every other value will be assigned `0`.

Softmax is a softer version of this function. Instead of returning `1` for the largest value and `0` for everything else, softmax returns a probability proportional to each value in the vector. This makes the third choice the correct answer to this question.

Finally, notice that the fourth choice is similar to the third one, but it talks about the "vector's maximum value." This would be a `max` function, not an `argmax`.

Running a vector through the `max` function returns the maximum value in that vector, not the index of where that value is located. From a probabilistic perspective, having the maximum value will not help create a vector of probabilities that sum up to 1, so the fourth choice is not a correct answer.

## References
- [Softmax Activation Function with Python](https://machinelearningmastery.com/softmax-activation-function-with-python/)
- [What is the Softmax Function](https://deepai.org/machine-learning-glossary-and-terms/softmax-layer)