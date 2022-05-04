
#Python 3.7.4
#pip install paho-mqtt

import time
#import paho.mqtt as mqtt
import paho.mqtt.client as mqtt
import ssl

# Thingstream > Location Services > PointPerfect Thing > Credentials
BrokerHost = 'pp.dev-svc.services.u-blox.com'
DeviceID = '0ca1cec5-efbf-4fbf-8612-eac4d7361910'
MQTT_TOPIC = [("/pp/ip/eu/unenc",0), ("/pp/ubx/0236/ip",0)]
#MQTT_TOPIC = [("/pp/ip/us/unenc",0)]

last_time = time.time()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
      print("Connected to broker!")
    else:
      print("Connection failed!")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  global last_time
  elapsed_time = time.time() - last_time
  print('Received', msg.topic, len(msg.payload), 'elapsed_time:', elapsed_time )
  last_time = time.time()


client = mqtt.Client(client_id=DeviceID)
client.on_connect = on_connect
client.on_message = on_message

#client.tls_set(
 # certfile='device-0ca1cec5-efbf-4fbf-8612-eac4d7361910-pp-cert.crt', keyfile='device-0ca1cec5-efbf-4fbf-8612-eac4d7361910-pp-key.pem')

client.tls_set(
  certfile='C:\LOGAN\BMW_AMBY\PPThing_BMW\device-0ca1cec5-efbf-4fbf-8612-eac4d7361910-pp-cert.crt', 
  keyfile='C:\LOGAN\BMW_AMBY\PPThing_BMW\device-0ca1cec5-efbf-4fbf-8612-eac4d7361910-pp-key.pem')

#client.tls_insecure_set(True)
client.connect(BrokerHost, port=8883)
client.subscribe(MQTT_TOPIC)
client.loop_forever()

