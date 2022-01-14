#external import
import paho.mqtt.client as mqtt
tele ='tele/'
cmnd ='cmnd/'
stat = 'stat/'
state = '/STATE'
sensor = '/SENSOR'
result = '/RESULT'
power = '/POWER#'

#internal import




# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):

	print("Connected with result code "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.

	client.message_callback_add(tele+"+"+state, node_db.updatetime) 
	client.message_callback_add(stat+"#", node_db.updatestate)

	client.subscribe(tele+"+"+state)
	(nodes,er) = node_db.read('*','',(1,))
	for row in nodes:
		client.subscribe(stat+row[2]+"/"+row[3])


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	#print(msg.topic.split('/'))
	#print(msg.topic+" "+str(msg.payload.decode("utf-8")))
	return 


def mqtt_init(config):

	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.username_pw_set(config["USER"], password=config["PASSWORD"])
	client.connect(config["BROKER_IP"])
	(nodes,er) = node_db.read('*','',(1,))
	for row in nodes:
		#print(cmnd+row[2]+"/"+row[3])
		client.publish(cmnd+row[2]+"/"+row[3], '')


	client.loop_forever()