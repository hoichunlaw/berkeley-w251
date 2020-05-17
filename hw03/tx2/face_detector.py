import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt

broker="mosquitto"
port=1883

def on_publish(client,userdata,result):
    print("data published \n")
    pass

# Define mqtt client and connect
client1 = mqtt.Client("face_detector")
client1.on_publish = on_publish
client1.connect(broker, port)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(1)

i = 0
while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # cut off faces and publish messages to local broker
    for (x,y,w,h) in faces:
        cv.rectangle(gray, (x,y), (x+w,y+h), (255,0,0),2)
        face_gray = gray[y:y+h, x:x+w]
        rc,png = cv.imencode('.png', face_gray)
        msg=png.tobytes()
        ret = client1.publish("face_images/gray", payload=msg, qos=0, retain=False)

cap.release()
