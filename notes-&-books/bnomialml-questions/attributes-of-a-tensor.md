# The attributes of a tensor

A "tensor" is one of the most basic data structures used in machine learning systems.

Let's go back to basics and focus on the fundamental characteristics of a tensor.

**Which of the following are valid attributes that represent a tensor?**

- [x] Its number of axes. This attribute is also called the "rank" of the tensor.
- [ ] Its cardinality. This attribute represents the numerical relationship between the axes of the tensor.
- [x] Its shape. This attribute represents the number of elements along each dimension.
- [x] Its data type. This attribute represents the type of values contained in the tensor.

## Answer

Three primary attributes define a tensor:

1. Its rank, or the number of axes.
2. Its shape, or the number of dimensions.
3. Its data type, or the type of data contained in it.

The rank of a tensor refers to the tensor's number of axes.

Examples:

- Rank of a matrix is 2.
- Rank of a vector is 1.
- Rank of a scalar is 0.

The shape of a tensor describes the number of elements along each dimension.

Examples:

- `()` — scalar
- `(2,)` — vector
- `(3, 2)` — matrix
- `(3, 2, 5)` — 3D tensor

The data type of a tensor refers to the kind of data contained in it.

Examples:

- `float32`
- `float64`
- `uint8`
- `int64`

The second choice mentions "the cardinality of a tensor" as "the numerical relationship between the axes of the tensor." This is not a correct answer.

In summary, the correct answer to the question is the first, third, and fourth choices.

## Reading

- [Deep Learning with Python, Second Edition](https://amzn.to/3K3VZoy) covers the topic of tensors really well.
- Check ["A Gentle Introduction to Tensors for Machine Learning with NumPy"](https://machinelearningmastery.com/introduction-to-tensors-for-machine-learning/) for a quick introduction to tensors and practical code.
