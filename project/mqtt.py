import datetime
from sqlalchemy import update
from flask import Blueprint
from flask_mqtt import Mqtt
from .models import Node
from . import app 
from . import db

mqtt_var = Mqtt()
mqtt = Blueprint('mqtt', __name__)


@mqtt_var.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt_var.subscribe('tele/+/STATE')
    #print ("connected")
    with app.app_context():
        node = Node.query.filter_by(category="lamp")
        for row in node:
            mqtt_var.subscribe('stat/'+row.topic+'/'+row.item_id)
        for row in node:
            mqtt_var.publish('cmnd/'+row.topic+'/'+row.item_id, None)


@mqtt_var.on_topic('stat/#')
def handle_switch(client, userdata, message):
    with app.app_context():
        #print('Received message on topic {}: {}'.format(message.topic, message.payload.decode()))
        db.session.query(Node).\
            filter(Node.topic == message.topic.split('/')[1], Node.item_id == message.topic.split('/')[2]).\
            update({'status':(message.payload == b'ON'),'last_update':datetime.datetime.now() }, synchronize_session="fetch")
        db.session.commit()
        #print (Node.query.filter_by(topic=message.topic.split('/')[1], item_id=message.topic.split('/')[2])[0].status)


@mqtt_var.on_topic('tele/+/STATE')
def handle_state(client, userdata, message):
    with app.app_context():
        #print('Received message on topic {}: {}'.format(message.topic, message.payload.decode()))
        db.session.query(Node).\
            filter(Node.topic == message.topic.split('/')[1]).\
            update({'last_update' : datetime.datetime.now() }, synchronize_session="fetch")
        db.session.commit()
        #for row in Node.query.filter_by(topic=message.topic.split('/')[1]):
        #    print (row.last_update)

@mqtt_var.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print("msg: "+message.topic)

