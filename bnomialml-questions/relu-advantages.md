# Daniella is looking at ReLU's advantages

Daniella knows that she can improve her deep learning model by replacing the activation funcion of some of the layers with Rectified Linear Unit (ReLU) functions.

Unfortunately, she knows there's going to be pushback from the team. There always is!

The best path forward is to prepare a list with some of advantages of ReLU. This ought to convince everyone to make the change.

Daniella prepares an initial draft, but she would like some help reviewing it right before sending it.

**Which of the following are advantages of using the ReLU?**

- [ ]  ReLU saturates around extreme values, allowing backpropagation to converge faster and helping the network learn.
- [x]  ReLU provides better representational sparsity than the *sigmoid* and *tanh* activation functions because it can produce an actual zero output.
- [x]  ReLU is computationally straightforward to implement.
- [x]  Neural networks are easier to optimize when their behavior is as linear as possible. ReLU acts mainly as a linear function, improving our ability to optimize neural networks.

## Let's take a look at the correct answer.

The first thing we need to do is remember that ReLU is a linear function that outputs the input directly if is positive or outputs zero otherwise:
`f(x) = max(0, x)`

The first choice argues that ReLU saturates around extreme values, which is incorrect. Other activation functions like *sigmoid* saturate around `0` and `1`, and *tanh* around `-1` and `1`, but ReLU works differently.

The second choice is correct since ReLU can turn any negative inputs into zero, unlike *sigmoid* and *tanh* that only learn to approximate a zero value. When using ReLU, we can have layers with one or more nodes containing zero values, which we call "sparse representation". This simplifies the model and accelerates learning.

The third choice is also correct since ReLU is very simple to implement. In comparison, *sigmoid* and *tanh* require exponentiation which is more expensive to compute.

Finally, neural networks are easier to optimize when their behavior is linear, and ReLU acts as a linear function for the most part. We call it a "piecewise linear function" because it's linear for half of the input domain and nonlinear for the other half. This is enough to affect the optimization process positively.

In summary, the last three choices are correct.

## References
* [A Gentle Introduction to the Rectified Linear Unit (ReLU)](https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks/)
* [Rectifier (neural networks)](https://en.wikipedia.org/wiki/Rectifier_(neural_networks))