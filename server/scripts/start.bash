#!/bin/bash

source venv/bin/activate
cd app
gunicorn -c ../gunicorn_config.py wsgi:app

