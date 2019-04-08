## Welcome to AWS_IOT Publishing

In this section I am trying to publishing a perticular topic to **AWS-IOT**.


### on_connect
This function will reconnect if we lose conection.

### To Configure network encryption and authentication options and enable SSL/TLS support
    mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

### To connect to AWS Host
    mqttc.connect(awshost, awsport, keepalive=60)
    
### Publishing the data to _AWS-IoT_
    mqttc.publish("$aws/things/ThingName/shadow/update", jsonMessage, qos=1)
