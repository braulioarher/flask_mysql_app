#!/bin/bash

pip install -r requirements.txt
avenv
export FLASK_APP=roomapp
export FLASK_DEBUG=1
flask run