import cv2 as cv
from PIL import Image, ImageDraw
import sys, os, urllib
import tensorflow.contrib.tensorrt as trt
import tensorflow as tf
import numpy as np
import time
from tf_trt_models.detection import download_detection_model, build_detection_graph
#import paho.mqtt.client as mqtt

FROZEN_GRAPH_NAME = 'frozen_inference_graph_face.pb'
DETECTION_THRESHOLD = 0.5

# load frozen graph
output_dir=''
frozen_graph = tf.GraphDef()
with open(os.path.join(output_dir, FROZEN_GRAPH_NAME), 'rb') as f:
  frozen_graph.ParseFromString(f.read())

INPUT_NAME='image_tensor'
BOXES_NAME='detection_boxes'
CLASSES_NAME='detection_classes'
SCORES_NAME='detection_scores'
MASKS_NAME='detection_masks'
NUM_DETECTIONS_NAME='num_detections'

input_names = [INPUT_NAME]
output_names = [BOXES_NAME, CLASSES_NAME, SCORES_NAME, NUM_DETECTIONS_NAME]

trt_graph = trt.create_inference_graph(
    input_graph_def=frozen_graph,
    outputs=output_names,
    max_batch_size=1,
    max_workspace_size_bytes=1 << 25,
    precision_mode='FP16',
    minimum_segment_size=50
)

tf_config = tf.ConfigProto()
tf_config.gpu_options.allow_growth = True

tf_sess = tf.Session(config=tf_config)
tf.import_graph_def(frozen_graph, name='')

tf_input = tf_sess.graph.get_tensor_by_name(input_names[0] + ':0')
tf_scores = tf_sess.graph.get_tensor_by_name('detection_scores:0')
tf_boxes = tf_sess.graph.get_tensor_by_name('detection_boxes:0')
tf_classes = tf_sess.graph.get_tensor_by_name('detection_classes:0')
tf_num_detections = tf_sess.graph.get_tensor_by_name('num_detections:0')

cap = cv.VideoCapture(1)

k = 0
while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    image_resized = np.array(cv.resize(image, (300,300)))
    image_np = np.array(image)

    start_time = time.time()
    scores, boxes, classes, num_detections = tf_sess.run([tf_scores, tf_boxes, tf_classes, tf_num_detections], feed_dict={
        tf_input: image_resized[None, ...]
    })
    elapsed_time = time.time() - start_time
    print("inference time", elapsed_time)

    boxes = boxes[0] # index by 0 to remove batch dimension
    scores = scores[0]
    classes = classes[0]
    num_detections = num_detections[0]

    for i in range(int(num_detections)):
        if scores[i] < DETECTION_THRESHOLD:
            continue
        # scale box to image coordinates
        box = boxes[i] * np.array([image_np.shape[0], image_np.shape[1], image_np.shape[0], image_np.shape[1]])

        # cut faces
        face = image[int(box[0]):int(box[2]), int(box[1]):int(box[3])]
        cv.imwrite("output/image" + str(k) + ".jpg", face)
        k += 1

cap.release()
