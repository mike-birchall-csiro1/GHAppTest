#!/usr/bin/bash
source ./setenvs.sh
echo ngrok config add-authtoken $NGROK_AUTHTOKEN
ngrok config add-authtoken $NGROK_AUTHTOKEN

