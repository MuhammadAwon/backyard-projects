# Australian birds

Marc was excited about the performance of his model.

He's been working on an app to classify photos of birds, and his model is performing very well on all metrics.

Marc knows what he is doing and followed all the best practices: he split training and test data, used the proper evaluations metrics, balanced his dataset, and reviewed examples regularly to ensure there were no labeling errors.

Finally, Marc launched his app.

Positive feedback started rolling in except from one place: users in Australia complained the performance was awful.

Marc was baffled.

**What is the most likely reason for the problem?**

- [ ] Marc didn't train the model long enough to capture all the necessary details of different bird species.
- [ ] Marc's model is too simple, and it couldn't learn the entire dataset of birds, leaving out those from Australia.
- [x] Marc's model suffers from sampling bias. He probably didn't include enough examples of Australian birds.
- [ ] Marc's model is suffering from data or concept drift.

## Answer

A common problem in machine learning is that a model that shows promising results during evaluation doesn't perform well when deployed in production.

While there may be various reasons for that, the story above points us in one particular direction.

Not training the model long enough is unlikely to be a problem here. Marc wouldn't be getting good results anywhere if this was the case. Notice that problems seem to only happen in Australia, so we can easily discard the first choice.

Insufficient model capacity can't either be a valid reason for what Marc is seeing. As we mentioned before, if this were the case, the model would be underfitting and give poor results across the board, not localized to a specific region.

Data and concept drift are indeed common problems with models in production. However, they arise when the environment changes over time, and so does the input to the model. In this case, the problem appeared straight after deployment.

This leaves us with the only correct answer: The most likely reason for this problem is that Marc didn't have enough data from Australia, so his model is struggling to recognize birds from that region.

This issue is called "sampling bias." It explains why the problem occurred in one particular country. Sampling bias is difficult to detect during development because the data is missing from the training and test datasets, so we can't notice it while evaluating the model.

In conclusion, the third choice is the correct answer to this question.

## References

- [Sampling bias](https://en.wikipedia.org/wiki/Sampling_bias)
- [Bird classification](https://xkcd.com/1425/)
