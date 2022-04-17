# The birthday paradox

After a lot of begging, Lucia convinced Anna to go to a party together.

Anna likes to spend most of her time with math books. The change of scenery was good, so she showed up.

After an hour or so, Lucia noticed that Anna was not having fun, so she decided to cheer her up with an interesting problem.

"Anna, there are 23 people at this party right now. What is the probability that two of them share the same birthday?"

**What is the correct answer to Lucia's question?**

- [ ] There's about a 1% probability of two people sharing the same birthday.

- [ ] There's about a 6% probability of two people sharing the same birthday.

- [ ] There's about a 17% probability of two people sharing the same birthday.

- [x] There's about a 50% probability of two people sharing the same birthday.

## Answer

This is an interesting question.

Most people go with `22/365` and end up with a `6%` probability. This answer, unfortunately, is wrong.

Let's think about the answer by simplifying the problem: given two people, what is the probability they share the same birthday?

Sometimes, it's useful to turn the problem around and focus on the opposite case: can we compute the probability of 2 people not sharing the same birthday? Let's see.

The first person's birthday is any day of the year, so there are `365` possibilities. The second person's birthday is any day of the year except the first person's birthday, so there are `364` possibilities.

In total, we have `365 * 364 = 13,2860` combinations where two people don't share a birthday. Since we are interested in the probability of two people sharing birthdays, we can use the following formula where `DO` refers to "desired outcomes" and `PO` to "possible outcomes":

```
P = 1 - (DO / PO)
P = 1 - ((365 * 364) / (365 * 365))
P = 1 - 99.72%
P = 0.0028
P = 0.28%
```

There's less than a `1%` probability of 2 people sharing birthdays. Using this, we can generalize our process to the 23 people at the party.

```
P = 1 - (365! / ((365 - 23)! * 365^23))
```

The math is rough at this point, but you can use [Wolfram Alpha](https://www.wolframalpha.com/input?i=1+-+%28365%21+%2F+%28%28365+-+23%29%21+*+365%5E23%29%29) to solve it for you.

```
P = 0.5072
P = 50%
```

So there you have it: There's about a `50%` probability of two people sharing the same birthday at the party.

## References

- [Birthday problem](https://en.wikipedia.org/wiki/Birthday_problem)
- [The Birthday Paradox](https://pudding.cool/2018/04/birthday-paradox/)
- [Let's test your probabilistic intuition!](https://twitter.com/TivadarDanka/status/1498465296260034561)
