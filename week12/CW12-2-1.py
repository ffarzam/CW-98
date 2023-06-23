from http.server import HTTPServer, BaseHTTPRequestHandler
import time

import json
HOST = "192.168.1.167"
PORT = 9999


class FarzamHttp(BaseHTTPRequestHandler):

    def get_response(self):
        return json.dumps({})

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))


server = HTTPServer((HOST, PORT), FarzamHttp)
print("Server listening on")
server.serve_forever()
server.server_close()
print("Server closed")