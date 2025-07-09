#!/bin/bash

cd ~/app
nohup python3 main.py > app.log 2>&1 &

