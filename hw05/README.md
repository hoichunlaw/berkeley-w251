# Homework 5

## 1. What is TensorFlow? Which company is the leading contributor to TensorFlow?

TensorFlow is the deep learning framework developed by Google Brain team. Leading contributor to TensorFlow is Google.

## 2. What is TensorRT? How is it different from TensorFlow?

TensorRT is a framework that is used for speeding up deep learning models' inference time. It is able to optimized deep learning models trained in different frameworks with the use of CUDA. 

## 3. What is ImageNet? How many images does it contain? How many classes?

ImageNet is an image database organized according to the WordNet hierarchy (currently only the nouns), in which each node of the hierarchy is depicted by hundreds and thousands of images. This dataset was designed by academics and intended for computer vision research. There are over 14 million of images and 21841 labels.

## 4. Please research and explain the differences between MobileNet and GoogleNet (Inception) architectures.

MobileNet is an efficient model built for mobile and embedded vision applications. Instead of standard convolutional layers, MobileNet factorizes standard conv layers into depthwise convolution and pointwise convolution, in order to reduce the number of parameters and computational cost.  

GoogLeNet's core architecture is the inception module. This module performs 1x1 convolutions followed by standard convolutions in order to reduce parameters.

## 5. In your own words, what is a bottleneck?

Bottleneck in neural network means a layer with less neurons then the layers below or above. This is a layer to compress information from input layer and extract the most efficient representation of input layer information with less dimensions. 

## 6. How is a bottleneck different from the concept of layer freezing?

Bottleneck is to reduce dimensions of input layer in order to filter out noise and genenate a more compact representation of information. Layer freezing just means freezing some layers' parameters during training, e.g. freezing the pre-trained network when performing transfer learning.

## 7. In part one this lab, you trained the last layer (all the previous layers retain their already-trained state). Explain how the lab used the previous layers (where did they come from? how were they used in the process?)

The previous layers are pre-trained layers from TensorFlow hub. The pre-trained layers generate feature vectors from images, then we pass these feature vectors to a fully connected softmax output layers. Then we train the parameters on this finaly softmax layers only with our training data.

## 8. Why is the batch size important? What happens if you try running with a batch size of 32? What about a batch size of 4?

Batch size is a hyperparameters for neural network training, it affects the training time and also model accuracy. Smaller batch size takes more time to train the network, vice versa, this is because smaller batch size makes gradient calculation and gradient updates more frequently. Larger batch size shorten the training time but this also sacrifices the model performance i.e. model accuracy.

## 9. Find another image classification feature vector from tfhub.dev and rerun the notebook. Which one did you pick and what changes, if any did you need to make?

I picked tf2-preview/inception_v3/feature_vector. I needed to change the image size, because inception_v3 needs input image size to be 299x299 instead of 224x224 used by MobileNet. Output feature vectors are with dimension of 2048 for inception_v3 compare to 1280 in mobilenet.

## 10. How long did the training take in part 2?

It took around 2 hours to train 50 epochs with batch size 10.

## 11. In part 2, you can also specifiy the learning rate using the flag --learning_rate. How does a low --learning_rate (part 2, step 4) value (like 0.001) affect the precision? How much longer does training take?

It did not affect accuracy but it takes 1.5x longer to train for each epochs. 

## 12. How about a --learning_rate (part 2, step 4) of 1.0? Is the precision still good enough?

Accuracy is around 10% worse than before, and the training time is similar.

## 13. For part 2, step 5, How accurate was your model? Were you able to train it using a few images, or did you need a lot?

I train a model to classify either an image is a building or forest. I used 1000 images for each category and I was able to achieve 99.94% accuracy.