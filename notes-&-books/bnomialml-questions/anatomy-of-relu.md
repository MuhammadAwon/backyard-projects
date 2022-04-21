# The anatomy of ReLU

The Rectified Linear Activation Function, or ReLU, returns its input if it's positive or a zero otherwise.

In other words: ReLU turns any negative values into zero and leaves everything else unmodified.

ReLU has become a popular activation function when training neural networks. Since it's a linear function and computationally straightforward to implement, models become easier to optimize and achieve better performance.

There's something very interesting about combining Gradient Descent with ReLU, and to get there, we have to think a bit about the mathematical properties of ReLU.

**Which of the following is true about the Rectified Linear Activation Function (ReLU)?**

- [ ] The function is neither continuous nor differentiable.
- [ ] The function is differentiable but not continuous.
- [ ] The function is both continuous and differentiable.
- [x] The function is continuous but not differentiable.

## Answer

Let's cut right to the chase: ReLU is continuous but not differentiable, which means the fourth choice is the correct answer.

While the function is indeed differentiable for values of `x>0` and `x<0`, it is not differentiable for `x=0`.

Think about it: what is the derivative of the ReLU function at `x=0`? Is it constant? Is it rising? The derivative is not defined at `x=0`, so the function is not differentiable.

This may be surprising because we know that Gradient Descent needs a differentiable function to work. How come it works with ReLU, then?

In a really good post about this topic, [Sebastian Raschka](https://twitter.com/rasbt) wrote about this:
> In practice, it’s relatively rare to have `x=0` in the context of deep learning, hence, we usually don’t have to worry too much about the ReLU derivative at `x=0`. Typically, we set it either to `0`, `1`, or `0.5`.

So there you have it. The correct answer to this question is the fourth choice.

## References

- [Why is the ReLU function not differentiable at x=0?](https://sebastianraschka.com/faq/docs/relu-derivative.html)
- [The anatomy of ReLU](https://typefully.com/svpino/the-anatomy-of-relu-39YF09b)
- [A Gentle Introduction to the Rectified Linear Unit (ReLU)](https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks/)
