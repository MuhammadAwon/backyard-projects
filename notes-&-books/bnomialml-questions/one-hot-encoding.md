# Alice can't remember how One-Hot Encoding works

When building a machine learning model, much of the work happens well before starting training.

Alice knows that she needs to prepare the data before it's ready. She has been looking into encoding some of the features on her dataset. One-Hot Encoding seems like a good candidate.

It's been quite a while since Alice used One-Hot Encoding, and she can use some help.

**Which of the following statements explains how One-Hot Encoding works?**

- [ ] One-Hot Encoding encodes a numerical feature into its categorical representation.
- [x] One-Hot Encoding creates additional features based on the number of unique values in a categorical feature.
- [ ] One-Hot Encoding encodes a string-encoded feature into its numerical representation.
- [ ] One-Hot Encoding encodes a string-encoded feature into its categorical representation.

## Answer

Categorical data are variables that contain label values rather than numeric values. For example, a variable representing the weather with values "sunny," "cloudy," and "rainy" is a categorical variable.

Although some algorithms can use categorical data directly, the majority can't. They require the data to be numeric.

One-Hot Encoding is a way to turn categorical data into a numerical representation.

The first choice is the opposite of how One-Hot Encoding works. The third and fourth choices talk about "string-encoded" features, which is not how it works either. This leaves us with only one possibility: the second choice.

One-Hot Encoding creates a new feature for each unique value of the original categorical variable. For example, in the case of our previous weather variable, One-Hot Encoding would create three new features: `sunny`, `cloudy`, and `rainy`, and it will assign the values `0` or `1` appropriately.

In summary, the second choice is the correct answer.

## References

- [Why One-Hot Encode Data in Machine Learning?](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/)
- [Here’s All you Need to Know About Encoding Categorical Data](https://www.analyticsvidhya.com/blog/2020/08/types-of-categorical-data-encoding/)
- [One hot](https://en.wikipedia.org/wiki/One-hot)
