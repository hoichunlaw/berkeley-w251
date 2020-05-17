import paho.mqtt.client as mqtt
import datetime
import os

os.popen('sh setup.sh')

LOCAL_MQTT_HOST="remotebroker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_images/gray"
path = "/mnt/face_images_gray/"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC, qos=0)

def on_message(client,userdata, msg):
  try:
    print("message received!")
    f = open(path+"hw03/"+datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%s"), "wb")
    f.write(msg.payload)
    f.close()
    
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message



# go into a loop
local_mqttclient.loop_forever()
