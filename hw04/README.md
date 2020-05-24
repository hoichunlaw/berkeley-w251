# Homework 4: DL 101

## Part 1 Q2

### Name all the layers in the network, describe what they do.

- 1st layer is input layer.  Input image is with size 24x24. Original images were with size 28x28. Author randomly cropped 24x24 pixels from orignal images to perform image augmentation.

- 2nd layer is convolutional layer, kernel size is 5x5, number of filters is 8. Stride is 1, which means the filters slide through pixels one by one. Padding of 2 is added. Activation function is relu.  

- 3rd layer is pooling layer, with size 2x2 and stride 2. This layer calculates the max value across all the 2x2 regions from previous layer.  

- 4th layer is convolutional layer, kernel size is 5x5, number of filters is 16, stride is 1, padding is 2 and activation function is relu. This is to perform convolutional operation again after max pooling.

- 5th layer is pooling layer, with size 3x3 and stride 3. This layer calculates the max value across all the 3x3 regions from previous layer.  

- 6th layer is output layer, with softmax output. Number of classes is 10. It calculates the probability of 10 classes that the image belongs to.  

### Experiment with the number and size of filters in each layer. Does it improve the accuracy?  

Accuracy improves with increasing number of filters, vice versa. Accuracy decreased with larger filters but accuracy didn't increase with smaller filters (comparing to default kernel size of 5x5).    

### Remove the pooling layers. Does it impact the accuracy?  

Removing the pooling layers lower the accuracy.  

### Add one more conv layer. Does it help with accuracy?

Adding one more conv layer does not help with accuracy. The reason is that, after the 2nd conv layer, the output size was 4x4x16. Performing another conv operation on 4x4 data may not be helpful in extracting information and constructing better decision boundaries.

### Increase the batch size. What impact does it have?

Increasing batch size from 20 to 1000, the network is slower to converge and accuracy decreased.

### What is the best accuracy you can achieve? Are you over 99%? 99.5%?

96%

## Part 1 Q3 

https://github.com/hoichunlaw/berkeley-w251/blob/master/hw04/w251_homework04.ipynb

## Part 2 Q1: What was the average inference time for model and image combination? What where the returned classes their score?  

### Inference Time
Model | parrot | polar_bear | mcqueen | sea_lion |  
--- | --- | --- | --- | ---  
efficientnet-L_quant.tflite | 1535ms | 1560ms | 1550ms | 1545ms |
efficientnet-M_quant.tflite | 595ms | 600ms | 620ms | 610ms |
efficientnet-S_quant.tflite | 385ms | 395ms | 390ms | 390ms |
inception_v4_299_quant.tflite | 1845ms | 1845ms | 1820ms | 1810ms |
mobilenet_v1_1.0_224_quant.tflite | 100ms | 98ms | 98ms | 98ms |
mobilenet_v2_1.0_224_quant.tflite | 75ms | 75ms | 70ms | 70ms |

### Score of correct class
Model | parrot | polar_bear | mcqueen | sea_lion |  
--- | --- | --- | --- | ---  
efficientnet-L_quant.tflite | 0.9336 | 0.8594 | 0.5273 | 0.8555 |
efficientnet-M_quant.tflite | 0.9375 | 0.9023 | 0.5313 | 0.9297 |
efficientnet-S_quant.tflite | 0.8789 | 0.8828 | 0.4531 | 0.9571 |
inception_v4_299_quant.tflite | 0.9961 | 0.9883 | 0.7931 | 0.9961 |
mobilenet_v1_1.0_224_quant.tflite | 0.9961 | 0.9961 | 0.5586 | 0.9961 |
mobilenet_v2_1.0_224_quant.tflite | 0 | 0 | 0 | 0 |

## Part 2 Q2: In your opinion, which model is best and why?

mobilenet_v1_1.0_224_quant.tflite is the best. It gives the fastest inference time and does not give up a lot of accuracy compare to inception_v4_299_quant.tflite.

## Part 2 Q3: Did the EfficientNet models return the correct classifiction? If not why, and how would you fix this?

It did not return the correct classification at the beginning. There is problem in mapping model output to class label. I changed the code in classifier.py to shift the mapping by 1 unit to match.

## Part 2 Q4: How big (in megabytes) are the models?

Model | size(MB) |
--- | ---
mobilenet_v1_100_224 | 15.13 |
mobilenet_v2_130_224 | 19.37 |
efficientnet b0 | 18.93 |
efficientnet b4 | 68.74 |
efficientnet b7 | 234 |

## Part 2 Q5: How did the performance compare to TFLite? Be sure to through out the first run as it includes downloading.

For mobilenet, TF1.15 achieved similar accuracy with faster inference time. For efficientnet, TF1.15 achieved faster inference time but somehow lower accuracy.

## Part 2 Q6: Compare the performance of TF2 to TF 1.15

All models achieved similar accuracies in TF2 and TF1.15. But the inference time is much longer in TF2.

## Part 2 Q7: What models did you use?

AlexNet, GoogleNet, ResNet-18, VGG-16

## Part 2 Q8: What was the average inference time for model and image combination? What where the returned classes their score?

### Inference Time
Model | parrot | polar_bear | mcqueen | sea_lion |  
--- | --- | --- | --- | ---  
AlexNet | 44ms | 43ms | 44ms | 48ms |
GoogleNet | 67ms | 65ms | 72ms | 60ms |
ResNet-18 | 48ms | 44ms | 46ms | 48ms |
VGG-16 | 141ms | 96ms | 151ms | 261ms |

### Score of correct class
Model | parrot | polar_bear | mcqueen | sea_lion |  
--- | --- | --- | --- | ---  
AlexNet | 0.9995 | 0.9966 | 0.8086 | 0.9957 |
GoogleNet | 0.9995 | 1.0000 | 0.6069 | 0.9980 |
ResNet-18 | 0.8608 | 0.9067 | 0.4490 | 0.9282 |
VGG-16 | 0.9995 | 1.0000 | 0.6475 | 1.0000 |

## Part 2 Q9: In your own words, what is quantization? What is effect on peformance and accuracy?

Quantization is to optimize the trained models into smaller in size and faster to run at inference time. The goal of quantization is to improve performance without sacrificing a lot of accuracy.

## Part 2 Q10: In your option, which framework was best? Why?

I would pick Jetson Inference framework. It faster to run for most models and it does not seem to sacrifice too much accuracy. One of the test images I have is a cartoon car McQueen, and Jetson Inference framework with model AlexNet give 80% score on correct label, which outperformed all other frameworks/models for this difficult classification.

## Codes & Images:

Images: https://github.com/hoichunlaw/berkeley-w251/tree/master/hw04/images  
TF 1.15 classifier: https://github.com/hoichunlaw/berkeley-w251/blob/master/hw04/classifier_tf1.15.py  
TF 2.0 classifier: https://github.com/hoichunlaw/berkeley-w251/blob/master/hw04/classifier_tf2.py  
Jetson Inference Classifier: https://github.com/hoichunlaw/berkeley-w251/blob/master/hw04/imagenet-console-v2.py  