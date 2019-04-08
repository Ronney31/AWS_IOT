'''
	Remember it won't work, as because till now we aren't storing our data to aws, so in order to 
	see the result we need to run the publish.py 

	**one limitation it subscribring to all the topics.
'''

import os
import socket
import ssl
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connection returned result: " + str(rc) )
	client.subscribe("#" , 1 )
	print("Connection established successfully")


def on_message(client, userdata, msg):
	print("Topic: "+msg.topic)
	print("Payload Data: "+str(msg.payload))
	print("*"*25)



mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "amazonaws.com"
# AWS Port(Default: 8883)
awsport = 8883
# Client ID
clientId = "thingName"
# Thing Name defined in AWS IoT
thingName = "thingName"
# Root Certificate Path
caPath = "rootCA1.pem"
# Certificate Path
certPath = ".pem.crt"
# Private Key Certificate Path
keyPath = "private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_forever()
