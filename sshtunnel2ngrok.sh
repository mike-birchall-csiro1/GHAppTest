#!/usr/bin/bash
source ./setenvs.sh
echo ngrok http --url=$NGROK_URL $PORT
ngrok http --url=$NGROK_URL $PORT
