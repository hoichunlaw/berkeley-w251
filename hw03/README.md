# Homework3 - Internet of Things 101

## Build Docker Images

### on TX2
Three container images were built, one for face detector, one for local broker, one for message forwarder.
```
docker build -t hw03/facedetector -f docker/Dockerfile_FaceDetector .
docker build -t hw03/localbroker -f docker/Dockerfile_LocalBroker .
docker build -t hw03/forwarder -f docker/Dockerfile_Forwarder .
```

### on Cloud
Two container images were built, one for remote broker, one for image processor.
```
docker build -t hw03/remotebroker -f Dockerfile_RemoteBroker .
docker build -t hw03/processor -f Dockerfile_ImageProcessor .
```