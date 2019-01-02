import logging
import sys

from flask import Flask

# Flask setup
app = Flask(__name__)

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


# Logging setup
app.logger.setLevel(logging.INFO)

#app.add_url_rule(BASE_URL, 'test', lights_handler.test)
if __name__ == '__main__':
    print('Starting app...')
    app.run(host='0.0.0.0', debug=True, port=5000)
