#!/bin/sh
LIB_LOCATION=venv/lib/python3.5/site-packages

cp $LIB_LOCATION/phue.py $LIB_LOCATION/phue.py.old
cp phue.py.fix $LIB_LOCATION/phue.py

