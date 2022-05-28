# Rolling down the hill

Brooklyn was dealing with a complex problem. Although gradient descent was working relatively well, she read that adding momentum could benefit her use case.

Brooklyn needed to justify spending more time on this problem, so she wrote an email summarizing her reasoning behind using momentum, hit send, and patiently waited for her manager to respond.

**Which of the following statements are some of the reasons that Brooklyn included in her email?**

- [x] Momentum helps when there's a lot of variance in the gradients.
- [x] Momentum helps overcome local minima.
- [x] Momentum helps the training process converge faster.
- [ ] Momentum helps when there aren't flat regions in the search space.

## Explanation

There's a problem with **gradient descent**: it depends entirely on the gradients it computes along the way, so whenever there's a lot of variance in these gradients, the algorithm can bounce around the search space making the optimization process slower.

Adding **momentum** to gradient descent will help overcome this problem. Here is Jason Brownlee on **"Gradient Descent With Momentum from Scratch"**:

> Momentum involves adding an additional hyperparameter that controls the amount of history (momentum) to include in the update equation, i.e. the step to a new point in the search space.

This parameter will help gradient descent accelerate in one direction based on past updates. A good analogy is a ball rolling down the hill. The more momentum it gains, the faster the ball will move in the direction of travel. If we have noisy gradients, momentum will help dampen the noise and keep the algorithm moving in the correct direction. Therefore, the first choice is correct.

This explanation also helps understand why the third choice is correct as well. Having gradients with a lot of variance will cause gradient descent to spend a long time bouncing around, while adding momentum will straighten the direction of the search. This will lead to faster convergence.

Momentum helps the optimization overcome small local minima by rolling past them. Going back to our example of a ball rolling down the hill, the more momentum it has, the more likely it will be to overcome small dips in the ground. This makes the second choice correct as well.

Finally, the fourth choice is not correct because momentum does help with flat regions in the search space. In the same way it can overcome small dips in the surface, momentum can help gradient descent get past a flat region by continuing its previous movement. Here is **Jason Brownlee** again:

> (...) momentum is helpful when the search space is flat or nearly flat, e.g. zero gradient. The momentum allows the search to progress in the same direction as before the flat spot and helpfully cross the flat region.

In summary, the first three choices are correct.

## Reading

- ["Gradient Descent With Momentum from Scratch"](https://machinelearningmastery.com/gradient-descent-with-momentum-from-scratch/)  covers this question very well and includes practical examples of how to implement momentum.
- ["Momentum"](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Momentum) is the Wikipedia page covering momentum as part of [Stochastic Gradient Descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent).
- The ["Deep Learning"](https://amzn.to/3CSjPkR) book by Goodfellow, et. al. is a fantastic source covering this topic.