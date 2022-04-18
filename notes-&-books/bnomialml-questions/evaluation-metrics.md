# Keeping pedestrians safe

A team has been working on a self-driving car model to detect pedestrians crossing the street on images captured from the car cameras.

Their model will help cars navigate busy areas while keeping everyone around safe. It's a critical and delicate piece to get to full autonomy.

Despite initial promising results, they haven't settled on the best way to evaluate the model's performance.

A discussion starts with some initial ideas.

**Which of the following evaluation metrics would be the best for this problem?**

- [ ] The team should use the recall of the model, as defined by the percentage of detected pedestrians with respect to every image containing a pedestrian.
- [ ] The team should use the precision of the model, as defined by the percentage of legitimate detected pedestrians with respect to every detected pedestrian.
- [x] The team should use the Fβ-Score of the model with a high value of β.
- [ ] The team should use the Fβ-Score of the model with a low value of β.

## Answer

Imagine mounting a video camera on your car and exporting every frame after a long day of driving.

Most likely, the vast majority of images will not show pedestrians. Well, I guess there's a chance that you only drive on busy city streets and get to see many more pedestrians, but for most drivers, this won't be the case.

This insight is essential. Detecting pedestrians on images captured from a car is an imbalanced problem; only a few photos will contain the class we care about: a person.

When working with imbalanced problems where the class you want to detect represents the minority of samples, neither recall nor precision will be a good metric by itself to evaluate the model.

For example, you can use the recall to understand how many pedestrians the model is detecting, but if the model flags every image as showing pedestrians, the recall will be 100%. This, of course, it's not helpful so we can discard the first and second choices of this question.

Using the Fβ-Score, however, is a good choice.

The Fβ score lets us combine precision and recall into a single metric. When using β = 1, we place equal weight on precision and recall. For values of β > 1, recall is weighted higher than precision; for values of β < 1, precision is weighted higher than recall.

You are probably familiar with F1-Score. F1-Score is just Fβ-Score with β = 1.

Now, to answer this question correctly, we need to determine if we want to prioritize recall or precision. This, however, is not always an easy task.

Let's say the team would instead report a pedestrian that is not there than miss somebody crossing the street. If the former happens, the car will probably break for no reason, but something worse could happen if we don't stop the car.

This seems to be a sensible choice, and if the team agrees, they should prioritize building a system with high recall, so using a higher value of β is the way to go.

This makes the third choice the correct answer.

## References

- [What is the F-Score?](https://deepai.org/machine-learning-glossary-and-terms/f-score)
- [A Gentle Introduction to the Fbeta-Measure for Machine Learning](https://machinelearningmastery.com/fbeta-measure-for-machine-learning)
- [F-score](https://en.wikipedia.org/wiki/F-score)
