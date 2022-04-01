from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random
import sys
import time
from threading import Thread
PORT = 9000
HOST = '0.0.0.0'

start = False;
n = 0

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
            for i in range(0, n):
                sensorsMock[i] = {'bpm': random.randint(80, 90), 'onFinger': True}
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
            for i in range(0, n):
                sensorsMock[i] = {'bpm': random.randint(80, 90), 'onFinger': True}
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
        if(len(sys.argv) > 1):
            n = int(sys.argv[1])
        print("The server has been planted! Running...")
        startHTTP_server()
    except KeyboardInterrupt:
        print("Exiting")
