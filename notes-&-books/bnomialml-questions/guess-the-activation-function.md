# Which function is she using?

Kiara was leaving her team, but she didn't want to go without having some fun.

She put together a simple neural network with one hidden layer. Never trained it, but she initialized its parameters and told her team that they should expect every node from the hidden layer to return a value resembling the following formula:
> y = max(0.01 * x, 0)

Kiara saved the model and asked her team to test the node results without looking at the code. They found out that, in effect, the results always followed the formula mentioned by Kiara.

Kiara's question to her team was simple:

**Which of the following activation functions am I using in this network?**

- [ ] Kiara is using the sigmoid activation function.
- [ ] Kiara is using the Rectified Linear Unit activation function.
- [x] Kiara is using the Leaky Rectified Linear Unit activation function.
- [ ] None of the above activation functions can produce this output.

## Answers

This is a fun, interesting question and one where we need to be very careful to find the correct answer.

The team doesn't have access to the network architecture, so all they know is that node outputs follow a specific pattern. They also know Kiara is using an activation function. If we use σ to represent this activation function, the result of each node should look like this:
> z = σ(y)

Here, `z` is the output the team is getting out of the node, and `y` is the input to the activation function. This input results from `y = w * x + b`, where `b` is the bias, and `w` is the weight assigned to that node. Putting everything together:
> z = σ(w * x + b)

Let's start with *sigmoid*, which doesn't use the `max` operation, so we can safely discard it.

Here is the formula of the *Leaky Rectified Linear Unit* (Leaky ReLU):
> y = max(0.01 * x, x)

This one looks promising, and it's how Kiara wanted to prank her team. Assuming that `x` results from `w * x + b`, Leaky ReLU would almost make sense, except it returns the maximum between a scaled version of `x` and `x`, while the team is seeing something different. Leaky ReLU can't possibly be the answer.

Here is the formula of the *Rectified Linear Unit* (ReLU):
> y = max(x, 0)

It looks similar, but where is the scaling factor? Well, Kiara initialized the network, so there's a good chance she did it in a way to confuse everyone. If Kiara set every weight `w` to be `0.01` and every bias term to be zero, we would get the following:
> z = σ(w * x + b)
>
> z = σ(0.01 * x + 0)

Assuming that σ is the ReLU activation function, we will get the following:
> z = max(0.01 * x + 0, 0)
>
> z = max(0.01 * x, 0)

This is the pattern the team is seeing. Kiara used ReLU as her activation function.

## References

- [A Gentle Introduction to the Rectified Linear Unit (ReLU)](https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks/)
- [Rectifier (neural networks)](https://en.wikipedia.org/wiki/Rectifier_(neural_networks))
- [Leaky ReLU](https://paperswithcode.com/method/leaky-relu)
- [Activation Functions](https://himanshuxd.medium.com/activation-functions-sigmoid-relu-leaky-relu-and-softmax-basics-for-neural-networks-and-deep-8d9c70eed91e)
