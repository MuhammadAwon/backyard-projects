# Peter needs a better balance

Peter is having a bad day.

He is working on a deep learning model that uses MRI images to classify a rare disease. Unfortunately, Peter has many more pictures from healthy people than people having the disease, and his model classifies every sample as healthy.

Collecting more data for such a rare disease is very difficult, and strict privacy regulations make the whole process even more problematic.

Peter needs another solution.

**What can Peter do to improve the model?**
- [x] Give higher weight to the samples showing the disease.
- [ ] Replace the deep learning model with a Decision Tree because the latter is more robust to imbalanced data.
- [x] Augment the dataset with slightly modified copies of the images showing the disease.
- [ ] Reduce the learning rate to allow the model to learn underrepresented samples.

## Answer!

Dealing with imbalanced datasets is a common problem in machine learning, and there are many strategies to deal with it. The solution is usually a combination of several approaches.

An approach that is usually easy to implement is giving the underrepresented classes higher weight in the loss function. This way, the model will be penalized more if it fails to detect one of the rare samples. Every major machine learning framework supports a parameter to control the weight assigned to each class, so "Give higher weight to the samples showing the disease" is a correct answer.

Another good approach to solve the problem is to augment the underrepresented class. Data augmentation is the process of creating new training data by applying slight modifications to existing samples. For instance: rotation, translation, skewing, color changes, among others. Using data augmentation, we can increase the size of the training dataset and make the model more robust to these variations. This makes the option "Augment the dataset with slightly modified copies of the images showing the disease" also a correct answer.

We can also deal with an imbalanced dataset by oversampling the underrepresented classes, downsampling the dominant class, and generating synthetic data.

Decision Trees suffer from the same problems when dealing with imbalanced data, and the learning rate will not affect how the model handles the underrepresented class. Therefore, none of the other two options are correct.

## References
* [Computer Vision: How to tackle the problem of class imbalance in image datasets?](https://medium.com/mlearning-ai/computer-vision-how-to-tackle-the-problem-of-class-imbalance-in-image-datasets-d4d0ca6bd5db)
* [4 Ways to Improve Class Imbalance for Image Data](https://towardsdatascience.com/4-ways-to-improve-class-imbalance-for-image-data-9adec8f390f1)