# Homework3 - Internet of Things 101

## Create Docker Images

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
docker build -t hw03/remotebroker -f docker/Dockerfile_RemoteBroker .
docker build -t hw03/processor -f docker/Dockerfile_ImageProcessor .
```

## Run Containers

### on TX2
```
# Create a bridge:
docker network create --driver bridge hw03

# Local Broker
docker run --name mosquitto --network hw03 -p 1883:1883 hw03/localbroker

# Message Forwarder
docker run --name forwarder --network hw03 hw03/forwarder

# Face FaceDetector
docker run -d --privileged --network hw03 -v /dev/video0:/dev/video0 hw03/facedetector
```

### on Cloud
```
# Create a bridge:
docker network create --driver bridge hw03

# Remote Broker
docker run --name remotebroker --network hw03 -p 1883:1883 hw03/remotebroker

# Image Processor
docker run --privileged --name processor --network hw03 hw03/processor
```

## Cloud Object Storage  

http://cloud-object-storage-v7-cos-standard-c5s.s3.jp-tok.cloud-object-storage.appdomain.cloud/  

## Naming of MQTT topic  

Topic name "face_images/gray" was chosen. Face Images is bigger the class of image category. Gray is the property of the images.

## Choice of QoS  

QoS = 0 was chosen for this application. Reasons below:  
1. This is image streaming from video captures, There are over 50 pictures streamed and save to cloud in every second. It is not very important to capture every single pictures, therefore QoS=0 should be a good choice.  
2. Networks bridge between containers and also network between forwarder and remote broker are all stable. QoS=0 should be enough for this application.  