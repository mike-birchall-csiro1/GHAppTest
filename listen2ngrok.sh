#!/usr/bin/bash
source ./setenvs.sh
echo python3 ngrok-ears.py $HOST $PORT
python3 ngrok-ears.py $HOST $PORT
