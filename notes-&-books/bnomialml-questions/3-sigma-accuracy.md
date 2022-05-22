# The 3-sigma accuracy

Clara and her team are working on a drone localization project.

They have developed a neural network model that uses drone cameras to determine its position in the world so the drone can come back and land at the same spot it took off.

Clara was discussing the latest evaluation results with her colleagues when Jan mentioned that their latest model reached a 3-sigma accuracy of 20cm.

Clara is new to the industry, and "3-sigma accuracy of 20cm" didn't make much sense.

**What does a "3-sigma accuracy of 20cm" mean in this context?**

- [ ] In 66.6% of the cases, the model's error is less than 20cm
- [ ] In 68.2% of the cases, the model's error is less than 20cm
- [ ] In 95.4% of the cases, the model's error is less than 20cm
- [x] In 99.7% of the cases, the model's error is less than 20cm

## Explanation

The 3-sigma accuracy is a common way to quantify the accuracy of a model when estimating a continuous variable. Here is a quote from **Wikipedia's explanation of the 68 - 95 - 99.7 rule**:
> In the empirical sciences, the so-called three-sigma rule of thumb (or 3σ rule) expresses a conventional heuristic that nearly all values are taken to lie within three standard deviations of the mean, and thus it is empirically useful to treat 99.7% probability as near certainty.

<img src="https://user-images.githubusercontent.com/1126730/169593614-ee0ecdf7-a262-41b3-943f-5ae6865afcc8.png" width="800" height="400" />

If we take a larger range from -2σ to 2σ, then 95.4% of a normally distributed dataset will fall in this interval. Finally, a 3σ interval will cover 99.73% of the samples.

Therefore, when we talk about a 3-sigma accuracy of 20cm, we mean that 99.73% of the model predictions are more accurate than 20cm (because they fall in the -3σ to 3σ interval). Thus, the correct answer is the fourth choice.

## Recommendations

- [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution#Standard_deviation_and_coverage)
- [68–95–99.7 rule](https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule)
