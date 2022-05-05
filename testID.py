from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random
import sys
import time
from threading import Thread
PORT = 9000
HOST = '0.0.0.0'

start = False;
n = 15

rand = []
devId = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

def getkey():
    global start
    while (True):
        key = input()
        if(key == 'f' and not start):
            start = True
            print("[+] Start Event")
        elif(key == 's' and start):
            start = False
            print("[-] Stop Event")
        time.sleep(0.5)

class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if ('/' in self.path):
            outJson = {}
            sensorsMock = {}
            outJson['start'] = start
            actives = 0
            for i in range(0, n):
                if(rand[i] % 2 == 0):
                    sensorsMock[i] = {'bpm': random.randint(80, 90), 'onFinger': True}
                    actives+=1
                else:
                    sensorsMock[i] = {'bpm': 80, 'onFinger': False}
            outJson['active'] = actives
            outJson['online'] = sensorsMock

        self.wfile.write(json.dumps(outJson).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if ('/' in self.path):
            outJson = {}
            sensorsMock = {}
            outJson['start'] = start
            actives = 0
            for i in range(0, n):
                if(rand[i] % 2 == 0):
                    sensorsMock[i] = {'bpm': random.randint(80, 90), 'onFinger': True}
                    actives+=1
                else:
                    sensorsMock[i] = {'bpm': 80, 'onFinger': False}
            outJson['active'] = actives
            outJson['online'] = sensorsMock

        self.wfile.write(json.dumps(outJson).encode())

def startHTTP_server():
    """Start the server."""
    server_address = ('', PORT)
    server_HTTP = HTTPServer(server_address, TestHandler)
    server_HTTP.serve_forever()

if __name__ == "__main__":
    print("Press f + Enter to simulate start event")
    print("Press s + Enter to stop event")
    try:
        Thread(target=getkey).start()
        for i in range(0, n):
            rand.append(random.randint(1,2))
        rand[0] = 2
        print("The server has been planted! Running...")
        startHTTP_server()
    except KeyboardInterrupt:
        print("Exiting")
