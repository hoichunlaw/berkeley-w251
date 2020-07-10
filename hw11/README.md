# Homework 11 -- More fun with OpenAI Gym!

## Link to Cloud Object Storage

https://s3.eu-de.cloud-object-storage.appdomain.cloud/hw11-video/videos.zip

## Summary

    - Initial model with 16 nodes on first layer and 8 nodes on second layer failed to converge
    - Model was able to converge by increasing nodes on first layer to 512 and nodes on second layer to 256
    - Changing activation function on second layer from relu to tanh while keeping relu on first layer improved model performance on test set (I think tanh out stabilized input for final linear layer, thus improved performance)
    - But using tanh for both first layer and second layer make the model slow to train / fail to converge.
    - Changing final layer activation from linear to softmax failed to converge
    - Changing epsilon decay from 0.995 to 0.9 made the model converge to "optimal" policy very fast. But performance on test set is poor. I think this is due to not enough exploration in early stage of training thus, decreased the robustness of model
    - Changing trainig termination condition from average reward of 200 to 220 improved the performance of model on test set. I was able to achieve average reward 250.71 on test set

## Answer To Questions

### What parameters did you change?

    - Number of nodes on first layer and second layer
    - Activation function of first layer, second layer and final layer
    - epsilon decay
    - training termination condition


### What values did you try?

I tried combinations of below parameters
    - first layer: 16, 32, 256, 512, 1024 nodes with activation relu or tanh
    - second layer: 8, 16, 128, 256, 512 nodes with activation relu or tanh
    - final layer: linear or softmax
    - epsilon decay: 0.995, 0.99, 0.9
    - training termination condition: 200 or 220

### Did you try any other changes that made things better or worse?

The first model that successfully converged was with 512 nodes in first layer and 256 nodes in second layer. Changing activation from relu to tanh in second layer and changing training termination condition from 200 to 220 helped to improve testing result. Decreasing number of nodes in first and second layer to 16/32 and 8/16 will make the model fail to converge. Epsilon decay of 0.9 will make the model faster to converge in training but result in poor performance in testing.

### Did they improve or degrade the model? Did you have a test run with 100% of the scores above 200?

The best model I have is below:
    - first layer: 512 nodes with relu activation
    - second layer: 256 nodes with tanh activation
    - final layer: linear
    - epsilon decay: 0.995
    - training termination condition: last 100 training achieved average reward 220

89 tests of of 100 tests have score over 200, achieved average testing score of 250.71.

### Based on what you observed, what conclusions can you draw about the different parameters and their values?

    - If number of nodes on first and second layers are too small, the model failed to converge
    - Beyond certain point, increasing number of nodes on first and second layers did not improve model performance
    - tanh activation function on second layer helped to improve the model by providing more stable values to final linear layer
    - Softmax activation on final layer will make model fail to converge
    - Small epsilon decay will make the model faster to converge (by doing less exploration over time) but final model did not performed well in testing. Model is less robust if not enough exploration was done during training.
    - Changing training termination condition from 200 to 220 improved model performance in testing set, as model was trained longer to achieve better performance

### What is the purpose of the epsilon value?

epsilon-greedy learning refers to instead of just following the best policy from previous training, the agent has some probabilities to explore other possible actions. Epsilon value is the probability for the agent to explore actions other than best action learnt from previous training.

### Describe "Q-Learning".

Q-learning is a model free reinforcement learning algorithm to learn a optimal policy given a state. Given past training episodes, dynamic programming is performed to use Q-Function to approximate the reward of the given state and action pairs. This iterative process of estimating reward of given state and action pairs is called Q-Learning.