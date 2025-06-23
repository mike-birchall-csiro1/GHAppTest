# SIMPLE WEBSOCKET LISTEN AND REACT PYTHON CODE
import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080         # Port to listen on (non-privileged ports are > 1023)

# If command line arguments supplied values for host and port then use those
if (len(sys.argv))>1: HOST=sys.argv[1]
if (len(sys.argv))>2: PORT=int(sys.argv[2])

# Construct the HTTP 200 OK response
status_line = "HTTP/1.1 200 OK\r\n"
headers = "Content-Type: text/html\r\n" \
          "Connection: close\r\n" # Indicate that the connection will be closed after this response
body = "<html><body><h1>Hello from ngrok-ears!</h1></body></html>"

# Calculate Content-Length if you want to include it
content_length = f"Content-Length: {len(body.encode('utf-8'))}\r\n"

ok_response = (status_line + headers + content_length + "\r\n" + body).encode('utf-8')


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(64*1024) # Buffer Size = 64K should be enogh for web apps.
                if not data:
                    break
                str=data.decode()
                print(f"Received: {str}")
                text_file = open("log.txt", "w")
                text_file.write(str)
                text_file.close()
                #conn.sendall(OK_RESPONSE.encode()) # data # Echo back the received data
                #conn.send_response(200)
                conn.send(ok_response)
