# Convolutions are the answer

Jane is arguing with her colleague.

They are creating a neural network model to classify images uploaded to the company website.

Jane wants to use a Convolutional Neural Network, but her colleague disagrees. Instead, he wants to keep things simple and use a fully-connected neural network.

Jane feels that a Convolutional Neural Network is the right tool for the job, but how can she convince her colleague?

**Which of the following are some characteristics of Convolutional Neural Networks that may be helpful for Jane?**

- [ ] Convolutional Neural Networks are usually shallower than fully-connected networks, making the training process easier and faster.
- [x] Using a Convolutional Neural Network requires fewer parameters than a fully-connected network.
- [x] The local structure of the image can be used more efficiently by a Convolutional Neural Network, resulting in much better features and performance.
- [x] Convolutional Neural Networks can learn a hierarchy of visual features similar to the human brain, which results in better performance.

## Answer

A [Convolutional Neural Network](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNN) is a much better choice when dealing with image classification problems than a fully-connected network.

The first choice is not correct. A CNN is more time and memory efficient than a fully-connected network, so we can use deeper networks with many layers, which is impossible in a fully-connected network. You should always expect CNNs to be deeper than fully-connected networks.

CNNs require fewer parameters than fully-connected networks and reuse the same set of parameters over the whole image. The number of weights in a convolutional layer depends on the kernel size and number of channels and not on the image resolution. For example, in the [AlexNet architecture](https://en.wikipedia.org/wiki/AlexNet), the five convolutional layers are responsible for only 4% of the parameters of the network. In comparison, the final three fully-connected layers contain the remaining parameters. This makes the second choice a correct answer.

One reason CNNs are very effective in dealing with pictures is that they exploit the local structure of images. Since pixels located next to each other tend to be related, convolutional kernels can capture this information, making the third option a correct answer.

Finally, a CNN can learn visual features of increasing complexity. The initial layers typically learn to recognize low-level details, like edges and colors, while deeper layers can handle more complex structures like corners and patterns. The final layers of a CNN can learn complex representations like faces or any complex objects. Therefore, the fourth choice is correct.

## Reading

- ["A Beginner’s Guide to Convolutional Neural Networks (CNNs)"](https://towardsdatascience.com/a-beginners-guide-to-convolutional-neural-networks-cnns-14649dbddce8) is a great introduction to CNNs.
- If you want to get deeper into how convolutions work, check out ["A guide to convolution arithmetic for deep learning".](https://arxiv.org/pdf/1603.07285.pdf)