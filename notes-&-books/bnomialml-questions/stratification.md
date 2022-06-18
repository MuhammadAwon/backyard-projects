# A dataset of car pictures

This is the first team that Delilah manages.

She didn't have much experience as a manager, but she knew how important it's for a new team to nail down their process.

A couple of weeks in, the team is working on classifying different car makes and models from pictures captured with smartphones.

As the first step, Delilah asked the team to ensure that each make and model of the cars they care about is properly represented in both the training and test sets. Delilah knows they need to avoid testing for classes that the model didn't see during training or vice versa.

**Which of the following is the correct term that refers to the process that Delilah asked her team to follow?**

- [ ] Delilah asked her team to cross-validate their dataset.
- [x] Delilah asked her team to stratify their dataset.
- [ ] Delilah asked her team to validate their dataset.
- [ ] Delilah asked her team to bootstrap their dataset.

## Answer

[Stratified sampling](https://en.wikipedia.org/wiki/Stratified_sampling) is a method of splitting a dataset to produce splits that contain a properly balanced set of samples.

Delilah is working on a classification problem. In her case, stratified sampling will ensure that her training and test sets have approximately the same percentage of class samples as the complete set.

For example, let's assume the dataset has 10,000 pictures of Audis and 30,000 pictures of Hondas. Delilah would like to ensure that the team keeps this ratio when splitting the data into training and test sets. If the group selects 32,000 total images to train a model, Delilah would like to see 8,000 pictures of Audis (25%) and 24,000 of Hondas (75%.)

Therefore, the second choice is the correct answer to this question.

Something else to mention: there's a process called **"Stratified Cross-Validation."** If you knew about this, you might have been tempted to select the first choice as a valid answer. Notice, however, that Delilah is not asking the team to validate a model yet. She is just focused on how to split the dataset.

## Readings

- ["Stratified sampling in Machine Learning"](https://medium.com/analytics-vidhya/stratified-sampling-in-machine-learning-f5112b5b9cfe) is a quick introduction to stratified sampling.
- Check ["What is Stratified Cross-Validation in Machine Learning?"](https://towardsdatascience.com/what-is-stratified-cross-validation-in-machine-learning-8844f3e7ae8e) for more information about stratified cross-validation.
