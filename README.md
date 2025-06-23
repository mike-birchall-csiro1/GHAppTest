# GHAppTest
A repository for testing GitHub apps

==============
NGROK Solution
==============
1) Make sure Python3 is installed
2) Install ngrok:
	sudo snap install ngrok
3) chmod u+x configure4ngrok.sh
4) chmod u+x sshtunnel2ngrok.sh
5) chmod u+x listen2ngrok.sh
6) Configure authentication 4 ngrok: 
	./configure4ngrok.sh
7) Create SSH Tunnel to NGROK:
	./sshtunnel2ngrok.sh
8) In another terminal execute the ngrok listener:
	./listen2ngrok.sh


