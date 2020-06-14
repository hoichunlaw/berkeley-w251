# Homework 7 - Neural face detection pipeline

## Q1 Describe your solution in detail. What neural network did you use? What dataset was it trained on? What accuracy does it achieve?

I changed the face detector script from OpenCV haarcascade default frontal face to neural network base one. The one I used is same as what used in the demo noteobook, from https://github.com/yeephycho/tensorflow-face-detection. This network was trained on [WIDERFACE dataset](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/). I did not measure the accuracy on this model, but from inference result, it achieved quite good accuracy.

To run my script, I need to build a docker container with attached docker file.
```
docker build -t tensorrt -f Dockerfile.tensorrt .
```

Then start up the docker container and run the inference script
```
docker run --privileged -d --rm --network host -v /data/hw07:/tmp --name tensorrt tensorrt
docker exec tensorrt bash /tmp/run_inference.sh
```

## Q2 Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system?

It achieved reasonable accuracy in my test. It is possible to use this network to further develop a production-grade system. The inference speed and accuracy are reasonable, but the concern is, if we further develop algorithms to identify some features on the face, it could make the inference slower.

## Q3 What framerate does this method achieve on the Jetson? Where is the bottleneck?

Average inference time is around 0.08s per frame on my Jetson, it translates to 12.5 frames per second. Bottleneck was the inference process, forward pass of network takes time to complete.

## Q4 Which is a better quality detector: the OpenCV or yours?

Neural network based one is better. The OpenCV default one could only detect front faces but not side faces. Also OpenCV one couldn't detect faces when someone put a face mask on but neural network based one could still identify the faces.

## Access to output images:

