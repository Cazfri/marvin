import logging
import sys

from flask import Flask
from flask.logging import default_handler

from flask_cors import CORS

# Flask setup
app = Flask('marvin')
CORS(app)

# Import routing entry points
import lights.request_handler as lights_handler

# Routing
BASE_URL = '/'

LIGHTS_URL = BASE_URL + 'lights/'
# GET /lights/status (Get all properties of lights)
app.add_url_rule(LIGHTS_URL + 'status',
                 'lights_status',
                 lights_handler.status,
                 methods=['GET'])

# POST /lights/on (turn on all lights)
app.add_url_rule(LIGHTS_URL + 'on',
                 'lights_on',
                 lights_handler.on,
                 methods=['POST'])

# POST /lights/off (turn off all lights)
app.add_url_rule(LIGHTS_URL + 'off',
                 'lights_off',
                 lights_handler.off,
                 methods=['POST'])

# GET /lights/scenes (Get possible scenes)
# POST /lights/scenes (Run scene)
app.add_url_rule(LIGHTS_URL + 'scenes',
                 'lights_scenes',
                 lights_handler.scenes,
                 methods=['GET', 'POST'])

# POST /lights/push (turn off all lights)
app.add_url_rule(LIGHTS_URL + 'push',
                 'lights_push',
                 lights_handler.push,
                 methods=['POST'])

# Python logger setup
logging.basicConfig(filename='../logs/marvin.log', format='[%(asctime)s] %(levelname)s: %(message)s')

# Logging setup
app.logger.setLevel(logging.INFO)

# Basic setup
app.port=5000
app.host='0.0.0.0'

# All done!
app.logger.info('Starting app...')

#app.add_url_rule(BASE_URL, 'test', lights_handler.test)
if __name__ == '__main__':
    app.run(debug=True)
