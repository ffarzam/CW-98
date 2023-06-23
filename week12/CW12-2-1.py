from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST = "192.168.1.167"
PORT = 8080

todo_lst = []


class FarzamHttp(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(todo_lst).encode("utf-8"))

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        post_body_str = json.loads(post_body)
        todo_lst.append(post_body_str)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write("Post has been done successfully".encode("utf-8"))


server = HTTPServer((HOST, PORT), FarzamHttp)
print("Server listening on")
server.serve_forever()
server.server_close()
print("Server closed")