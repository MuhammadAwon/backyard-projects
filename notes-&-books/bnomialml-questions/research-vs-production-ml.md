# Research vs production

A common question among people new to artificial intelligence is about the path they would like to pursue.

Many opt for an academic role, where they can spend time doing research. Others prefer getting an industry job, where they get to experience putting machine learning systems into production.

Kathy isn't sure yet, so we will counsel her by highlighting some differences between both paths.

**Select every statement that correctly highlights the differences between machine learning modeling in a research environment versus production machine learning.**

- [x] The data used in a research environment is usually static, while the data used in a production setting is dynamic and constantly shifting.
- [x] The design priority in a research environment is usually higher performance—either the highest accuracy or other relevant metrics. Production environments put more emphasis on costs, scalability, and explainability.
- [ ] Research is usually not concerned with fairness, but fairness is crucial when building models in a production environment.
- [ ] When building machine learning models in a research environment, most of the work goes towards monitoring and maintaining models. In production environments, most of the work centers around the initial training and validation of the model.

## Answer

Kathy's story is not unique. In my experience, this is one of the most frequent questions I hear from people coming into the industry.

Although this question doesn't cover every difference, it's a good start, so let's start from the top.

Researchers like to test their work on popular datasets. This gives them a fair comparison with other existing methods and ensures its easy to reproduce their results. On the other hand, production data is constantly shifting. The datasets you used to train and test your models can quickly become obsolete. Therefore, the first choice is correct.

A lot of emphasis on academia centers around better algorithms and techniques. Can we solve this particular problem and do it more accurately? Can we do it faster? Research jobs are about inventing new methods and squeezing as much as we can from what we already know.

The focus on better techniques and algorithms leads to the main priority in many research positions: achieving better "performance." It could be about higher accuracy, a faster method, or fewer constraints. These, however, aren't usually the same concerns in the industry.

Production machine learning is generally more focused on the interpretability of results and the cost of the solution. "Higher accuracy" is not the most critical metric in many cases—it's still important but usually not at the expense of other factors. This is one of the main differences between a research position and an industry job. Therefore, the second choice is also correct.

Fairness is crucial. Yes, fairness is fundamental when putting machine learning into production, but it's equally necessary for any research environment. Therefore, the third choice is not correct.

Finally, in production environments, creating an initial model is just a small portion of work. After that, most of the time goes towards monitoring the model's results and maintaining it to **combat concept and data drift**. Conversely, in academia, the goal is usually to build a model. Since data is primarily static, models don't suffer any drift. Therefore, the fourth choice is incorrect.

In summary, the first and second choices are the correct answer to this question.

## Readings

- The ["Machine Learning Data Lifecycle in Production"](https://www.coursera.org/learn/machine-learning-data-lifecycle-in-production) course in Coursera, part of the [Machine Learning Engineering for Production (MLOps) Specialization.](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops)
- Check ["Why You Should Care About Data and Concept Drift"](https://evidentlyai.com/blog/machine-learning-monitoring-data-and-concept-drift) to understand the importance of monitoring machine learning models.
- ["A Gentle Introduction to Concept Drift in Machine Learning"](https://machinelearningmastery.com/gentle-introduction-concept-drift-machine-learning/) is an excellent introduction to concept drift.
