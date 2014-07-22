import socket
import json
import config
import sys

def getNames():
    ip = config.ip
    port = config.port

    sock = socket.socket()
    try:
        sock.connect((ip, port))
    except:
        sys.exit("Server is down.")

    else:
        data = {"cmd":"getNames"}
        data = json.dumps(data)
        sock.send(data)
        out = ""
        data = sock.recv(1024)
        while data:
            out += data
            data = sock.recv(1024)
        
        return json.loads(out)['songs']
