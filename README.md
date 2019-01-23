# mqttroute-elasticsearch-connector

This plugin connects Bevywise MQTT Broker with the ElasticSearch to store received payload info into ElasticSearch for further analysis and Visualization. 

# MQTTRoute 

Bevywise MQTT Broker is a powerful and high performance MQTTBroker that enables communication between various MQTT Devices and MQTT Sensors. MQTTRoute has FREE and affordable premium versions. 

# configure and setup mqttroute-elasticsearch-connector

	1. Open plugin.conf and configure 
		1.update hostname and port no of the Elastic search.
		2.update log file path to your own folder location. [default = Bevywise/MQTTRoute/extensions]
	2. Copy the plugin.conf and paste it in to Bevywise/MQTTRoute/extension.
	3. Copy the folder Elastic and paste it in to Bevywise/MQTTRoute/extensions.
	4. Replace custom_store.py with Bevywise/MQTTRoute/extensions/custom_store.py.
	5. Open Bevywise/MQTTRoute/conf/data_store.conf 
		1. Update CUSTOMSTORAGE = ENABLED
		2. Update DATASTORE = ELASTIC 
	6. Start the MQTTRoute and it will start storing all the payload into ElasticSearch Server.
