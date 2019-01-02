# Marvin
My very own smart home API

## What is this?
This is a Flask API server that controls smart home appliances. The server is deployed using Nginx and Supervisord, and orchestrated with Docker. Currently it only controls Phillips Hue bulbs, but the server API can easily be extended for other appliances.

## How does it work?
Currently, the Flask server is being run on a Raspberry Pi, which sends HTTP requests to other appliances. Right now the only way to interface with it is through the command line interface, but I'm planning on writing a graphical interface later.

To bring up the server with docker, use `docker-compose up`.

To bring it up with just Python, install the required packages (preferably in a virtualenv with `python3 -m virtualenv server/venv; source server/venv/bin/activate`) with `pip3 install -r server/requirements.txt`, then run `python3 server/app/main.py`.

To run the command line interface, first install the required packages with `pip3 install -r cli/requirements.txt`. You can make single requests to the CLI with commands such as `python3 cli/marvin.py lights on`, or start interactive mode by runninh `python3 cli/marvin.py`.

## Can I use this in my own setup?
You can, but currently this project is very specific to my personal needs. The code isn't designed to be used everywhere. This is meant to act as an example or starting point for similar projects. Feel free to fork or copy anything you see, but I make no guarantees that anything will work as intended.
