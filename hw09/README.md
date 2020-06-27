# Homework 9: Distributed Training and Neural Machine Translation

## File Submission and Screenshots

### nohup.out: https://github.com/hoichunlaw/berkeley-w251/tree/master/hw09/nohup.out

### BLEU Score on val set
![Validation BLEU curve](BLEU_Score.png)

### Train Loss
![Train loss curve](Train_Loss.png)

### Eval Loss
![Validation loss curve](Eval_Loss.png)

## Answer to Questions

### How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)

I left the training to run overnight for 7 hours. 18900 steps were completed.

### Do you think your model is fully trained? How can you tell?

The model is still not yet fully trained. From tensorflow board, we can see training loss and validation loss still going down. For fully trained model, we should pass a point where training loss still going down and validation loss going up. (model passed the optimal point and started to get overfitting)

### Were you overfitting?

No. As mentioned in previous question, training loss and val loss were still going down when I stopped the training.

### Were your GPUs fully utilized?

Yes. I could see ~100% usage of GPU memory for both containers.

### Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?

The max transfer speed between containers is 1000 Mbps. From nmon I can see the two containers were transferring data at 200 Mbps. Looks like network speed was not the bottleneck of training.

### Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?

Learning rate increased and then decreased. 