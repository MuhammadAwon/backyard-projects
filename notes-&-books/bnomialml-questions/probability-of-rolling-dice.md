# Rolling two dice

I have a bag in front of me containing a 6-sided and a 12-sided dice.

My friend pulls one out at random, rolls it, and tells me that the result is 3.

**What is the probability that my friend pulled out the 6-sided die?**

- [ ] The probability is 1/3
- [ ] The probability is 1/2
- [x] The probability is 2/3
- [ ] The probability is 3/4

## Answer

Let's assume that `A` represents the event of rolling the die and getting a `3`, `B1` represents the event of pulling out the 6-sided die, and `B2` represents the event of pulling out the 12-sided die.

We can compute the probability of my friend holding the 6-sided die using the **Bayes theorem**:

```
P(B1|A) = (P(A|B1)*P(B1))/P(A)
P(B1|A) = (1/12)/P(A)

P(A) = P(A∣B1)*P(B1)+P(A∣B2)*P(B2)
P(A) = 1/12 + 1/24​
P(A) = 1/8

P(B1|A) = (1/12)/(1/8)
P(B1|A) = 2/3​
```

Thus, the answer is `2/3`.

## Reading

- ["A Gentle Introduction to Bayes Theorem for Machine Learning"](https://machinelearningmastery.com/bayes-theorem-for-machine-learning/) is a great starting point to understand the Bayes theorem and how to use it.
- You can also check the Wikipedia page of [the Bayes theorem.](https://en.wikipedia.org/wiki/Bayes%27_theorem)
