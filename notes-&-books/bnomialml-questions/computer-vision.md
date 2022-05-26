# But why deep learning?

Martin met an old friend for a coffee.

They discussed Martin's latest work on image classification using deep learning. While Martin's friend used to work in computer vision 12 years ago, he is not aware of any of the latest developments.

He asks Martin why deep learning is so successful in image classification compared to the classical computer vision methods. He's heard that deep learning is better but doesn't understand why.

**If Martin wanted to summarize his reasoning with one sentence, which of the following is the best way to explain why deep learning is better for computer vision tasks?**

- [ ] Deep neural networks have many fully connected layers making the model more powerful.
- [x] Deep neural networks can learn the best features for the task, while traditional methods rely on engineered features.
- [ ] Deep learning methods can use much larger datasets and achieve better performance.
- [ ] Deep learning algorithms can take advantage of GPUs, and we can therefore train much larger and more powerful models.

## Explanation

These options explain why deep learning methods can achieve good results on computer vision tasks, but not all explain why deep learning is better than classical computer vision methods.

Having more data and algorithms optimized for GPUs can improve the results of a model. However, this is not exclusive to deep learning methods. Many traditional machine learning models can handle large datasets and take advantage of GPUs. Therefore, neither the third nor fourth choices correctly explain why deep learning is better for computer vision tasks.

The first choice is also incorrect. Although deep learning models can use many fully connected layers, the main benefits when solving computer vision problems come from using specialized layers—like convolutional layers—and not fully connected ones.

Finally, traditional computer vision methods typically rely on pre-computed features. Contrast this with **Convolutional Neural Networks** and **Vision Transformers**, which can learn features directly from the dataset and don't need pre-computed features to provide good results.

The ability to learn powerful features is one of the main reasons for the superior performance of deep learning methods in computer vision, making the second choice the best explanation for Martin's friend.

## References

- Here is an introduction to ["Convolutional Neural Networks"](https://en.wikipedia.org/wiki/Convolutional_neural_network).
- And this is the introduction to ["Vision Transformers"](https://en.wikipedia.org/wiki/Vision_transformer).
- ["Learned Features"](https://christophm.github.io/interpretable-ml-book/cnn-features.html) is an excellent explanation covering the features that we can learn using convolutional layers.
- Check out ["OpenAI Microscope"](https://openai.com/blog/microscope/) for a fascinating look at the visual features inside a neural network.
