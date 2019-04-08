var awsIot = require('aws-iot-device-sdk');

var device = awsIot.device({
    keyPath:'private.pem.key' , //private
    certPath: '-certificate.pem.crt',
    caPath: 'rootCA1.pem',
    clientId:'thingsName',
    host:'-1.amazonaws.com'
});

var contents ="Started.....!!!!";

device
    .on('connect',function () {

        console.log('connected');
        device.publish('$aws/things/thingsName/shadow/update',JSON.stringify({"state":{"reported":{"test_value1":500,"test_value2":250,"test_value3":96}}}));
        console.log('Message Sent...');

    });

device
    .on('message',function (topic,payload) {
        console.log('message',topic,payload.toString());
    });
