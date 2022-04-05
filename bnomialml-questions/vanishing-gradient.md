# Eliana knew the answer immediately

Eliana showed up early to the phone call.

Her agency has been advising a client who started building a deep learning model. Unfortunately, they've been stuck for a while, and it's Eliana's job to get them back on track.

Eliana realized what was happening ten minutes into the call.

When training their network and during the backpropagation process, the gradients quickly decrease until they approach zero, leaving the weights of the lower layers essentially unchanged.

Eliana knows this is the vanishing gradient problem. All that's left is to speculate about why this is happening.

**Which of the following are valid reasons for the model to suffer from the vanishing gradient problem?**

- [x] The hidden layers of the model use the Sigmoid activation function.
- [ ] The hidden layers of the model use the ReLU activation function.
- [x] The hidden layers of the model use the Tanh activation function.
- [ ] The model uses batch normalization.

## Answer!

Both the sigmoid and tanh activation functions have a common characteristic: they saturate when their input grows extremely large or small. Sigmoid saturates at `0` and `1`. Tanh saturates at `-1` and `1`. In both cases, the derivatives are very close to zero. When using these two activation functions in a deep neural network, it's not uncommon to face the vanishing gradient problem. This means that both the first and third choices are correct answers.

ReLU, on the other hand, is a way to solve the vanishing gradient problem. ReLU is much less likely to saturate, and its derivative is `1` for values larger than zero. This means that the second choice is an incorrect answer.

Finally, batch normalization is another way to mitigate the vanishing gradient problem. If we normalize the input to a layer that's using a sigmoid activation function, the values won't reach the edges and will stay instead around the area where the derivative isn't too small. Therefore, the fourth choice is also incorrect.

In summary, the correct answers are the first and third choices.

## References

* [Can ReLU Cause Exploding Gradients if Applied to Solve Vanishing Gradients?](https://analyticsindiamag.com/can-relu-cause-exploding-gradients-if-applied-to-solve-vanishing-gradients/)
* [How to Fix the Vanishing Gradients Problem Using the ReLU](https://machinelearningmastery.com/how-to-fix-vanishing-gradients-using-the-rectified-linear-activation-function/)
* [Vanishing gradient problem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem)