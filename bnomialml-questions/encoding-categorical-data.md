# Helping Madeline remember

Madeline is trying to complete her class assignment.

She just joined a machine learning program, and over the first few weeks, they have been talking about structured data and the different feature types we usually encounter.

Her task seems very simple: remove every ordinal feature from a dataset.

There's only one problem: Madeline doesn't remember what ordinal features are.

**Which of the following definitions correctly summarizes what an ordinal feature is?**

- [ ] An ordinal feature is a categorical variable with many possible values.
- [ ] An ordinal feature is a categorical variable with few possible values.
- [ ] Any feature used in a machine learning model is an ordinal feature.
- [x] An ordinal feature is a categorical variable with a meaningful order.

## Answer!

An ordinal feature is a categorical variable that comprises a finite set of discrete values with a ranked ordering between them.

Having a meaningful order between the values of an ordinal feature is very important. For example, you could have a feature to represent a person's economic status with three possible values: low, medium, and high. Notice how there's a clear order among these values.

The number of possible values does not limit an ordinal feature, so the first two choices aren't correct answers. The third choice is also not correct since a machine learning model could use features that aren't ordinal.

In summary, only the last choice is correct.

## References
* [Ordinal and One-Hot Encodings for Categorical Data](https://machinelearningmastery.com/one-hot-encoding-for-categorical-data/)
* [Here’s All you Need to Know About Encoding Categorical Data](https://www.analyticsvidhya.com/blog/2020/08/types-of-categorical-data-encoding/)
* [Ordinal data](https://en.wikipedia.org/wiki/Ordinal_data)