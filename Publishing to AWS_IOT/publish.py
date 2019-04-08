import os
import socket
import ssl
import paho.mqtt.client as mqtt
from time import sleep

connection_flag = False

# Check if the Connection to AWS Cloud has been Made.
def on_connect(client, userdata, flags, rc):
	global connection_flag
	connection_flag = True
	print("Connection returned result: " + str(rc) )

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

# Define the AWS Host Key, AWS PORT, Client Id, Thing Name, Root Certificate Path, Certificate Path, Private Key Certificate Path  
awshost = ".amazonaws.com"
# AWS Port(Default: 8883)
awsport = 8883
# Client ID
clientId = "ThingName"
# Thing Name defined in AWS IoT
thingName = "ThingName"
# Root Certificate Path
caPath = "root.pem"
# Certificate Path
certPath = ".pem.crt"
# Private Key Certificate Path
keyPath = "private.pem.key"

# Configure network encryption and authentication options
# Enable SSL/TLS support
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

# Connect to AWS Host
mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

while True:
	if connection_flag :

		# to off the motor
		jsonMessage = "{ \"state\": { \"reported\": {\"test_value1\":100,\"test_value2\":250,\"test_value3\":96} } }"
		mqttc.publish("$aws/things/ThingName/shadow/update", jsonMessage, qos=1)
		print ("Successfully Published for Turning Off Motor")
		sleep(5.0)

		# to on the motor
		jsonMessage = "{ \"state\": { \"reported\": {\"test_value1\":500,\"test_value2\":250,\"test_value3\":96} } }"
		mqttc.publish("$aws/things/ThingName/shadow/update", jsonMessage, qos=1)
		print ("Successfully Published for Turning On Motor")
		sleep(5.0)
	else:
		print("Waiting for Connection...")

ser.close()
