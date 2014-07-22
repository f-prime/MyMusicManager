import socket
import config
import json
import sys
import os

def getSong(song):
    sock = socket.socket()
    try:
        sock.connect((config.ip, config.port))
    except:
        sock.close()
        sys.exit("Could not connect.")
    
    else:
        data = {"cmd":"getSong", "song":song}
        sock.send(json.dumps(data))
        
        with open("tmp", 'wb') as file:
            while True:
                data = sock.recv(1024)
                if data:
                    file.write(data)
                else:
                    break
        
        return "tmp"
