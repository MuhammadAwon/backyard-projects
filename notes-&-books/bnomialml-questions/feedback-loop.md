# Mia and the feedback loop

Mia was crushing her thesis!

She was about to release a new neural network architecture that promised to raise the bar on image classification problems.

Mia did not start from scratch. She modified an existing model but added a key ingredient: feedback loops.

A feedback loop is when connections between units form a directed cycle, thus creating loops in the network. This gave Mia's network the ability to save information in the hidden layers.

Mia did a lot of research before deciding in favor of this architecture. She knew the advantages of her decision.

**Which was the architecture that Mia studied to learn about feedback loops?**

- [x] Recurrent Neural Networks
- [ ] Convolutional Neural Network
- [ ] Multilayer Perceptron
- [ ] Radial Basis Function Network

## Answer

Recurrent Neural Networks have an advantage over traditional feed-forward networks when working with time series or data points that depend upon previous samples.

The magic ingredient of Recurrent Neural Networks is the ability to store the information of previous inputs to generate the following output of the sequence. Recurrent Neural Networks do this by implementing the concept of a "feedback loop" or "feedback connection." These are connections feeding the hidden layers of the neural network back into themselves.

Neither Convolutional Neural Networks, Multilayer Perceptrons, nor [Radial Basis Function Networks](https://en.wikipedia.org/wiki/Radial_basis_function_network) supports the concept of feedback loops. Only Recurrent Neural Networks do.

Long Short-Term Memory (LSTM) networks are a type of Recurrent Neural Network very popular for sequence prediction problems.

## References

- [An Introduction To Recurrent Neural Networks And The Math That Powers Them](https://machinelearningmastery.com/an-introduction-to-recurrent-neural-networks-and-the-math-that-powers-them/)
- [Recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network)
- [A Gentle Introduction to Long Short-Term Memory Networks by the Experts](https://machinelearningmastery.com/gentle-introduction-long-short-term-memory-networks-experts/)
