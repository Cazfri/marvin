import logging

from flask import request, jsonify, abort, Flask
from lights.hue import HueController

log = logging.getLogger('flask.app')

def status():
    log.info('Returning status')
    sample_status = {'lights': 'on'} # TODO: Get lights status here
    if request.method == 'GET':
        return response(sample_status)
    else:
        return error_response('Method ' + request.method + ' not allowed', 405)

def on():
    log.info("Setting lights on")
    HueController().set_all_lights(True)
    return response()

def off():
    log.info("Setting lights off")
    HueController().set_all_lights(False)
    return response()

def scenes():
    if request.method == 'GET':
        scenes = HueController().get_scenes()
        print(scenes)
        return response([{'id': scene.scene_id, 'name': scene.name} for scene in scenes])
    elif request.method == 'POST':
        if not 'application/json' in request.headers['Content-Type']: # TODO: This could probably be if request.json
            return error_response('Invalid content-type: only json requests are accepted', 400)
        scene_name = request.json['sceneName']
        HueController().load_scene(scene_name)
        log.info("Running scene " + scene_name)
        return response()
    else:
        return error_response('Method ' + request.method + ' not allowed', 405)

def push(): # TODO: Finish this
    print(request.json)
    log.info("Setting lights to status: {}".format())
    return response()

def response(data = None, status = 200):
    if data:
        response = jsonify(data)
        response.status_code = status
        return response
    else:
        response = jsonify()
        response.status_code = status
        return response

def error_response(error_message, status = 500):
    return response({'error': error_message}, status)
