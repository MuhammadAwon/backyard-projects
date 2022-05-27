# Choosing a loss function

Ariana and Zach need to compute how different their model predictions are from the expected results.

They have been going back and forth between two different loss functions: Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE). These two functions have properties that will shine depending on the problem they want to solve.

**Which of the following is the correct way to think about these two loss functions?**

- [x] RMSE penalizes larger differences between the predictions and the observations.
- [ ] RMSE is significantly faster to compute than MAE.
- [ ] From both metrics, RMSE is the only one indifferent to the direction of the error.
- [ ] From both metrics, MAE is the only one indifferent to the direction of the error.

## Explanation

When we train a machine learning model, we need to compute how different our predictions are from the expected results. For example, if we predict a house's price as `$150,000`, but the correct answer is `$200,000`, our "error" is `$50,000`.

There are multiple ways we can compute this error, but two common choices are:

- RMSE — **Root Mean Squared Error**
- MAE — **Mean Absolute Error**

These have different properties that will shine depending on the problem we want to solve. Remember that the optimizer will use this error to adjust the model. We want to set up the right incentives so the model learns appropriately.

Let's focus on a critical difference between these two metrics. Remember the "squared" portion of the RMSE? You are "squaring" the difference between the prediction and the observed value. Here is the formula:

![](https://user-images.githubusercontent.com/1126730/170704538-41528db5-fcb0-4fe9-bdf1-e3af1880ddc9.png)

Since we square the errors before we average them, RMSE gives high importance to large errors. This means that our model will penalize larger differences between the observed and predicted values. The following table contains the calculation of RMSE and MAE for a few observations. Notice how the Error² column changes in comparison to the |Error|:

<img src='https://user-images.githubusercontent.com/1126730/170705158-d2943d25-30e4-44aa-a96b-dff8b9c36554.png' width='800' height='500'/>

MAE doesn't have the same property. The error increases proportionally with the difference between predictions and observations. Here is MAE's formula:

![](https://user-images.githubusercontent.com/1126730/170704910-4204daf4-9b5a-46c6-bbc7-4ce65df4eff1.png)

Predicting a house's price is a good example where `$10,000` off is twice as bad as `$5,000`. We don't necessarily need to rely on RMSE here, and MAE may be all we need.

But predicting the pressure of a tank may work differently. While 5 psi off may be within the expected range, 10 psi off may be a complete disaster. Here "10" is much worse than just two times "5", so RMSE may be a better solution.

Looking at the first choice, we already know it is the correct answer. RMSE penalizes larger differences between predictions and expected results.

Looking at both formulas, RMSE has extra squaring and root squaring operations, so it can't be faster to compute than MAE. The second choice is, therefore, not correct.

The third choice states that RSME is indifferent to the direction of the error, but MAE isn't. This is not correct: MAE uses the absolute value of the error, so both negative and positive values will end up being the same.

The fourth choice states that MAE is indifferent to the direction of the error, but RMSE isn't. This is not correct either: RMSE squares the error, so both negative and positive values will be the same.

In summary, the only correct answer to this question is the first choice.

## Reading

- ["RMSE vs MAE, which should I use?"](https://stephenallwright.com/rmse-vs-mae/) this is a great summary by Stephen Allwright about the properties of these two functions and how you should think about them.
- ["Root-mean-square deviation"](https://en.wikipedia.org/wiki/Root-mean-square_deviation) is the Wikipedia page covering RMSE.
- ["Mean absolute error"](https://en.wikipedia.org/wiki/Mean_absolute_error) is the Wikipedia page covering MAE.