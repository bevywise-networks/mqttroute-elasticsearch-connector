# mqttroute-elasticsearch-connector

This plugin connects MQTTRoute with the ElasticSearch to store received payload info into ElasticSearch for further analysis and Visualization. 

# MQTTRoute 

MQTTRoute is a powerful and high performance MQTTBroker that enables communication between various MQTT Devices and MQTT Sensors. MQTTRoute has FREE and affordable premium versions. 

# configure and setup mqttroute-elasticsearch-connector
	1. open plugin.conf and configure the hostname and port no.
	2. copy the  pugin.conf and paste it in to Bevywise/MQTTRoute/lib.
	3. copy the  folder Elastic and paste it in to Bevywise/MQTTRoute/lib.
	4. replace custom_store.py with Bevywise/MQTTRoute/lib/custom_store.py.
