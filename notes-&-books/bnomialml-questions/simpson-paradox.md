# Simpson's paradox

Natalia is developing a computer vision model to classify images of birds using a CNN.

She has a dataset of 20,000 images, split 50% into training and testing. The dataset is well balanced, containing an equal amount of bird and non-bird photos.

After some work, Natalia's model gets to around 90% accuracy, but she knows she can do better. It turns out that the model is not good at detecting birds from Madagascar, so Natalia asks her team to collect more data.

After several days, the data collection and labeling team provides 1,000 well-balanced new labeled images, which Natalia splits in half to extend the existing training and testing datasets.

The accuracy of the new model dropped to 88%.

**Which of the following is the approach that Natalia should follow to fix the problem?**

- [ ] There must be a problem with the labels on the last batch of 1,000 images from Madagascar. Natalia should work with the labeling team to correct the labels.
- [ ] The architecture of the CNN model is no longer valid for the new batch of data. Natalia should recalibrate the network to ensure she gets a better result.
- [x] The accuracy here might not tell the story of what's happening. Natalia should evaluate the model on the original 10,000-image test dataset for a valid comparison.
- [ ] Better data always leads to a better model, so Natalia should review her code because the accuracy must improve or stay where it was.

## Answer

Natalia compared the 90% accuracy computed on the 10,000 test images to the 88% accuracy on the augmented test dataset containing 10,500 images. There is a problem with this.

What if the new images from Madagascar are just much more difficult for the network? Even if the model improved, Natalia would not realize it because the additional pictures are causing the overall accuracy to drop.

Here is a hypothetical scenario of two models illustrating how the new model could improve even when returning a lower accuracy:

- Old model's accuracy on the 10,000 test images: 90% (9,000 images correctly classified.)
- Old model's accuracy on the new 500 test images: 10% (50 images correctly classified.)
- New model's accuracy on the 10,000 test images: 91% (9,100 images correctly classified.)
- New model's accuracy on the new 500 test images: 28% (140 images correctly classified.)
- New model's accuracy on the 10,500 test images: 88% (9,240 images correctly classified.)

In this hypothetical example, the new model is better on the original 10,000 test images (from 90% to 91%) and the 500 new images (from 10% to 28%.) However, the approach used by Natalia to evaluate the results made us believe the model got worse (going down from 90% to 88% accuracy.)

This is called the **Simpson's paradox**. When comparing two experiments, we need to make sure that we evaluate the same data or at least data having the same underlying distribution. If we change the distribution, we can't compare the results anymore and may take the wrong conclusion. Therefore, the third choice is the correct answer.

The wrong labels or architecture could be reasons for the model performing worse. However, we need to check if the model is performing worse in the first place, so assuming this is the case is premature.

The fourth choice is also not correct. Adding more data doesn't automatically mean better results.

## Reading

- Check ["Simpson's Paradox"](https://www.britannica.com/topic/Simpsons-paradox) for a complete explanation about the paradox.
- If you prefer videos, [watch this video](https://blog.chriszacharias.com/page-weight-matters) about the Simpson's Paradox.
