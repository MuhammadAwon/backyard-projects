# Breaking a function down into pieces

We are trying to predict the price of a car.

Our company has a website where users sell and buy used cars. Deciding how much we should charge for a used car is complicated and error-prone.

We want to build an automatic price recommendation system using supervised learning.

The Manufacturer's Suggested Retail Price (MSRP) of the car is our target variable. Since its distribution has a very long tail, we apply a log transformation before training the model.

**If our model for a single observation is `y = f(x)`, what are `x` and `y` for this project?**

- [x] `x` is a feature vector containing the variables that describe the car, and `y` is the logarithm of the price of the car.
- [ ] `x` is a feature vector containing the variables that describe the car, and `y` is the price of the car.
- [ ] `y` is a feature vector containing the variables that describe the car, and `x` is the logarithm of the price of the car.
- [ ] `y` is a feature vector containing the variables that describe the car, and `x` is the price of the car.

## Answer

Here we have a model that predicts the price of the car. We can think of the "model" as a function, albeit a complex one.

The good news is that we don't care what the actual function looks like. We can think of it as `y = f(x)`.

This function has two components: the function's output —or `y` value— and the function's input —or `x` value.

In our example, the result of that function is what we are looking to predict: the car's price. That means that `y` represents the car's price. On the other hand, `x` is a feature vector containing all of the other variables that we use to train our model. These could include the color of the car, the make, model, year, etc.

We can rule out this question's third and fourth choices by understanding this.

We have two possibilities left: the result is the car price or a logarithmic transformation of the price.

Remember that we trained this model using the logarithm of the target variable, which means our model can't output the price directly. Instead, the model's output will always be the logarithm of the car's price.

Therefore, the first choice is the correct answer to this question.

## References

- [How Machine Learning Algorithms Work](https://machinelearningmastery.com/how-machine-learning-algorithms-work/)
- [Machine Learning Bookcamp](https://amzn.to/3hCGbgo)
- [Log Transformation: Purpose and Interpretation](https://medium.com/@kyawsawhtoon/log-transformation-purpose-and-interpretation-9444b4b049c9)
