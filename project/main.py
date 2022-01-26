from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Node
from .mqtt import mqtt_var


main = Blueprint('main', __name__)

@main.route('/')
def index():
    nodes = Node.query.filter_by(category='lamp')
    return render_template('index.html', nodes=nodes)

@main.route('/', methods=['POST'])
def index_post():
    nodes = Node.query.filter_by(category='lamp')
    if 'bt1' in request.form:
        i=0
        for row in nodes:
            nodes[i].status = 1
            mqtt_var.publish('cmnd/'+ nodes[i].topic + '/' + nodes[i].item_id, 'ON')
            i=i+1

    elif 'bt2' in request.form:
        i=0
        for row in nodes:
            nodes[i].status = 0
            mqtt_var.publish('cmnd/'+ nodes[i].topic + '/' + nodes[i].item_id, 'OFF')
            i=i+1
    else:
        i=0
        for row in nodes:
            if row.name in request.form:
                if row.status == 0:
                    mqtt_var.publish('cmnd/'+ nodes[i].topic + '/' + nodes[i].item_id, 'ON')
                    nodes[i].status = 1
                else:
                    mqtt_var.publish('cmnd/'+ nodes[i].topic + '/' + nodes[i].item_id, 'OFF')
                    nodes[i].status = 0
            i=i+1

    return redirect(url_for('main.index'))


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

