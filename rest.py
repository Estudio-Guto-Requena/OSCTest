from http.server import HTTPServer, BaseHTTPRequestHandler
import json

PORT = 9000
HOST = '0.0.0.0'

BPM = 80

class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if ('/getbpm' in self.path):
            outJson = {"bpm": BPM, "onFinger": True}
        else:
            outJson = {"success": True}
        self.wfile.write(json.dumps(outJson).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if ('/getbpm' in self.path):
            outJson = {"bpm": BPM, "onFinger": True}
        else:
            outJson = {"success": True}
        self.wfile.write(json.dumps(outJson).encode())

def startHTTP_server():
    """Start the server."""
    server_address = ('', PORT)
    server_HTTP = HTTPServer(server_address, TestHandler)
    server_HTTP.serve_forever()

if __name__ == "__main__":
    try:
        print("The server has been planted! Running...")
        startHTTP_server()
    except KeyboardInterrupt:
        print("Exiting")
