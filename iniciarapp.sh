#!/bin/bash

pip install -r requirements.txt
avenv
export FLASK_APP=main.py
export FLASK_DEBUG=1
