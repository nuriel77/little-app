from flask import Flask
from flask import request
from random import randint
from time import sleep
import json
import os

app = Flask(__name__)

POD_IP = os.environ.get('POD_IP')
POD_HOSTNAME = os.environ.get('POD_HOSTNAME')
NODE_IP = os.environ.get('NODE_IP')

@app.route('/')
def index():
    obj = {
      "client_ip": request.remote_addr,
      "pod_ip": POD_IP,
      "pod_hostname": POD_HOSTNAME,
      "node_ip": NODE_IP
    }
    sleep_seconds = request.args.get('sleep', default='rand', type=str)

    if sleep_seconds == 'rand':
        sleep(randint(5, 30))
    else:
        sleep(int(sleep_seconds))

    return json.dumps(obj, indent=4)

@app.route('/healthz')
def healthz():
    """Respond to health check request."""
    return 'OK'
