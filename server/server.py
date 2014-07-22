import socket
import os
import json
import thread

class Server:
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 5555
        self.sock = socket.socket()

    def getSong(self, obj, song):
        with open("music/"+song, 'rb') as file:
            obj.send(file.read())

        obj.close()
    

    def getNames(self, obj):
        out = {"songs":os.listdir("music")}
        out = json.dumps(out)
        print out
        obj.send(out)
        obj.close()


    def main(self):
         self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
         self.sock.bind((self.host, self.port))
         self.sock.listen(5)
         while True:
            obj, conn = self.sock.accept()
            thread.start_new_thread(self.handle, (obj,))

    def handle(self, obj):
        data = obj.recv(1024)
        data = json.loads(data)
        if data['cmd'] == "getSong":
            self.getSong(obj, data['song'])

        elif data['cmd'] == "getNames":
            self.getNames(obj)
        

if __name__ == "__main__":
    Server().main()
