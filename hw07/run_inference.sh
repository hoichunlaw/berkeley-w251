cd /tmp
# download model
wget https://github.com/yeephycho/tensorflow-face-detection/blob/master/model/frozen_inference_graph_face.pb?raw=true -O frozen_inference_graph_face.pb

python3 face_detector_hw07.py
