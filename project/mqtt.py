from flask import Blueprint
from flask_mqtt import Mqtt
from models import Node

mqtt = Blueprint('mqtt', __name__)

from . import db
mqtt_var = Mqtt()

@mqtt_var.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt_var.subscribe('tele/+/STATE')
    print ("connected")


@mqtt_var.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data)
