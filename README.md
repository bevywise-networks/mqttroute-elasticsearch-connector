# mqttroute-elasticsearch-connector
The Connector to store the received events and commands published from the MQTTRoute - mqtt broker to the ElasticSearch backend. 

# configure and setup mqttroute-elasticsearch-connector
	1. open plugin.conf and configure the hostname and port no.
	2. copy the  pugin.conf and paste it in to Bevywise/MQTTRoute/lib.
	3. copy the  folder Elastic and paste it in to Bevywise/MQTTRoute/lib.
	4. replace custom_store.py with Bevywise/MQTTRoute/lib/custom_store.py.
